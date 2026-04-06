from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from aggregation import collect_metabolism_stats

SIGNAL_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_OPERATIONAL_STATES = {
    "precursor",
    "declared",
    "validated",
    "runnable",
    "invoked",
    "recorded",
    "validation_failed",
    "invoke_failed",
    "signal_unhandled",
    "registration_failed",
}


@dataclass
class ValidationIssue:
    severity: str
    code: str
    message: str
    location: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "location": self.location,
        }


@dataclass
class ValidationResult:
    workspace: Path
    issues: list[ValidationIssue] = field(default_factory=list)
    checked_files: list[str] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def add(self, severity: str, code: str, message: str, location: str) -> None:
        self.issues.append(ValidationIssue(severity, code, message, location))

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    def to_dict(self) -> dict[str, Any]:
        return {
            "validation": {
                "workspace": str(self.workspace),
                "status": "passed" if not self.errors else "failed",
                "checked_files": self.checked_files,
                "stats": self.stats,
                "issues": [issue.as_dict() for issue in self.issues],
            }
        }


class BeingValidator:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.result = ValidationResult(workspace=workspace)
        self.receptors_by_skill: dict[str, set[str]] = {}
        self.receiver_index: dict[str, set[str]] = {}
        self.membrane_paths: list[Path] = []
        self.total_log_invocations = 0

    def load_yaml(self, path: Path) -> Any:
        self.result.checked_files.append(path.relative_to(self.workspace).as_posix())
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}

    def validate(self) -> ValidationResult:
        self._validate_presence()
        self._load_receptors()
        self._validate_membranes()
        self._validate_phylogeny()
        self._validate_metabolism()
        self._validate_signals()
        self._validate_vitals()
        self.result.stats.update(
            {
                "membrane_count": len(self.membrane_paths),
                "receptor_count": len(self.receptors_by_skill),
                "log_invocations": self.total_log_invocations,
                "error_count": len(self.result.errors),
                "warning_count": len(self.result.warnings),
            }
        )
        return self.result

    def _validate_presence(self) -> None:
        required_paths = [
            self.workspace / ".being" / "homeostasis" / "vitals.yaml",
            self.workspace / ".being" / "phylogeny" / "tree.yaml",
            self.workspace / ".being" / "signals" / "receptors",
            self.workspace / ".being" / "metabolism",
            self.workspace / "organisms",
        ]
        for path in required_paths:
            if not path.exists():
                self.result.add("error", "missing-path", "Required path is missing", path.relative_to(self.workspace).as_posix())

    def _load_receptors(self) -> None:
        receptors_dir = self.workspace / ".being" / "signals" / "receptors"
        if not receptors_dir.exists():
            return
        for path in sorted(receptors_dir.glob("*.yaml")):
            data = self.load_yaml(path)
            skill = data.get("skill")
            receptors = data.get("receptors", [])
            if not skill:
                self.result.add("error", "missing-skill", "Receptor file missing skill field", path.relative_to(self.workspace).as_posix())
                continue
            signals: set[str] = set()
            for receptor in receptors:
                signal = receptor.get("signal")
                if not signal:
                    self.result.add("error", "missing-signal", "Receptor entry missing signal", path.relative_to(self.workspace).as_posix())
                    continue
                if not SIGNAL_RE.match(signal):
                    self.result.add("warning", "legacy-signal-name", "Signal name should migrate to kebab-case", f"{path.relative_to(self.workspace).as_posix()}::{signal}")
                signals.add(signal)
                self.receiver_index.setdefault(signal, set()).add(skill)
            self.receptors_by_skill[skill] = signals

    def _validate_membranes(self) -> None:
        for path in sorted(self.workspace.glob("organisms/**/**/*.membrane.yaml")):
            self.membrane_paths.append(path)
            data = self.load_yaml(path)
            identity = data.get("identity", {})
            name = identity.get("name")
            location = path.relative_to(self.workspace).as_posix()
            if not name:
                self.result.add("error", "missing-identity-name", "Membrane missing identity.name", location)
                continue
            parent_dir_name = path.parent.name
            stem_name = path.name.replace(".membrane.yaml", "")
            if parent_dir_name != name or stem_name != name:
                self.result.add("warning", "path-mismatch", "Membrane path does not match directory-style naming convention", location)
            ingress = data.get("ingress", [])
            egress = data.get("egress", [])
            if not ingress:
                self.result.add("error", "missing-ingress", "Membrane must declare at least one ingress", location)
            if not egress:
                self.result.add("error", "missing-egress", "Membrane must declare at least one egress", location)
            signals = data.get("signals", {})
            receives = signals.get("receives", [])
            emits = signals.get("emits", [])
            receptors = self.receptors_by_skill.get(name, set())
            for signal in receives + emits:
                if not SIGNAL_RE.match(signal):
                    self.result.add("warning", "legacy-signal-name", "Membrane signal should migrate to kebab-case", f"{location}::{signal}")
            for signal in receives:
                if signal not in receptors:
                    self.result.add("warning", "missing-receptor-alignment", "Membrane receive signal missing matching receptor entry", f"{location}::{signal}")
            for signal in emits:
                if signal not in self.receiver_index:
                    self.result.add("warning", "unhandled-emission", "No receptor currently listens to emitted signal", f"{location}::{signal}")

    def _validate_phylogeny(self) -> None:
        tree_path = self.workspace / ".being" / "phylogeny" / "tree.yaml"
        if not tree_path.exists():
            return
        data = self.load_yaml(tree_path)
        all_entities: list[dict[str, Any]] = []
        for group in ("prokaryotes", "eukaryotes"):
            all_entities.extend(data.get(group, []))
        for entity in all_entities:
            entity_id = entity.get("id", "<unknown>")
            state = entity.get("operational_state")
            if state not in ALLOWED_OPERATIONAL_STATES:
                self.result.add("error", "bad-operational-state", "Unknown operational_state value", f".being/phylogeny/tree.yaml::{entity_id}")
            membrane = entity.get("membrane")
            if membrane:
                membrane_path = self.workspace / membrane
                if not membrane_path.exists():
                    self.result.add("error", "missing-membrane-file", "Phylogeny points to a missing membrane file", f".being/phylogeny/tree.yaml::{entity_id}")
        self.result.stats["phylogeny_entities"] = len(all_entities)

    def _validate_metabolism(self) -> None:
        metabolism_dir = self.workspace / ".being" / "metabolism"
        if not metabolism_dir.exists():
            return
        for path in sorted(metabolism_dir.glob("*.log.yaml")):
            data = self.load_yaml(path)
            if not isinstance(data, list):
                self.result.add("error", "bad-log-format", "Metabolism log must be a YAML list", path.relative_to(self.workspace).as_posix())
                continue
            for index, item in enumerate(data):
                self.total_log_invocations += 1
                for key in ("invocation_id", "timestamp", "skill", "energy", "products", "outcome"):
                    if key not in item:
                        self.result.add("error", "missing-log-field", f"Metabolism record missing {key}", f"{path.relative_to(self.workspace).as_posix()}[{index}]")
                energy = item.get("energy", {})
                if "tokens_total" not in energy:
                    self.result.add("error", "missing-tokens-total", "Metabolism record missing energy.tokens_total", f"{path.relative_to(self.workspace).as_posix()}[{index}]")
        self.result.stats["metabolism_logs"] = len(list(metabolism_dir.glob("*.log.yaml")))

    def _validate_signals(self) -> None:
        signals_dir = self.workspace / ".being" / "signals" / "neurotransmitters"
        if not signals_dir.exists():
            return
        for path in sorted(signals_dir.glob("*.yaml")):
            data = self.load_yaml(path)
            signal = data.get("signal", {})
            name = signal.get("name")
            if not name:
                self.result.add("error", "missing-signal-name", "Signal file missing signal.name", path.relative_to(self.workspace).as_posix())
                continue
            if not SIGNAL_RE.match(name):
                self.result.add("warning", "legacy-signal-name", "Signal file name should migrate to kebab-case", path.relative_to(self.workspace).as_posix())
            target = signal.get("target")
            if target and name not in self.receptors_by_skill.get(target, set()):
                self.result.add("warning", "signal-target-unmatched", "Signal target does not declare a matching receptor", path.relative_to(self.workspace).as_posix())
            for consumer in signal.get("consumed_by", []):
                if name not in self.receptors_by_skill.get(consumer, set()):
                    self.result.add("warning", "signal-consumer-unmatched", "Consumed signal is not registered on consumer receptor list", path.relative_to(self.workspace).as_posix())

    def _validate_vitals(self) -> None:
        vitals_path = self.workspace / ".being" / "homeostasis" / "vitals.yaml"
        if not vitals_path.exists():
            return
        data = self.load_yaml(vitals_path)
        operational_status = data.get("operational_status")
        metabolism = data.get("vitals", {}).get("metabolism", {})
        aggregated = collect_metabolism_stats(self.workspace)
        total_invocations = metabolism.get("total_invocations", 0)
        if total_invocations != aggregated["total_invocations"]:
            self.result.add(
                "error",
                "invocation-count-mismatch",
                "vitals total_invocations does not match metabolism log count",
                ".being/homeostasis/vitals.yaml",
            )
        if metabolism.get("total_tokens_consumed") != aggregated["total_tokens_consumed"]:
            self.result.add(
                "error",
                "token-total-mismatch",
                "vitals total_tokens_consumed does not match metabolism log aggregation",
                ".being/homeostasis/vitals.yaml",
            )
        if metabolism.get("average_efficiency") != aggregated["average_efficiency"]:
            self.result.add(
                "error",
                "average-efficiency-mismatch",
                "vitals average_efficiency does not match metabolism log aggregation",
                ".being/homeostasis/vitals.yaml",
            )
        if metabolism.get("last_activity") != aggregated["last_activity"]:
            self.result.add(
                "error",
                "last-activity-mismatch",
                "vitals last_activity does not match metabolism log aggregation",
                ".being/homeostasis/vitals.yaml",
            )
        if operational_status == "operationally-alive" and total_invocations <= 0:
            self.result.add(
                "error",
                "alive-without-invocations",
                "operationally-alive requires at least one recorded invocation",
                ".being/homeostasis/vitals.yaml",
            )


def write_report(workspace: Path, result: ValidationResult) -> Path:
    output_dir = workspace / ".being" / "validation"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "latest.validation.yaml"
    with output_path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(result.to_dict(), handle, allow_unicode=True, sort_keys=False)
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the minimum Being runtime state.")
    parser.add_argument("workspace", nargs="?", default=".", help="Path to the Being workspace")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    validator = BeingValidator(workspace)
    result = validator.validate()
    report_path = write_report(workspace, result)

    print(f"Validation report written to: {report_path}")
    print(f"Errors: {len(result.errors)} | Warnings: {len(result.warnings)}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
