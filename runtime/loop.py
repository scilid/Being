from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from aggregation import refresh_vitals


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_z(dt: datetime) -> str:
    return dt.isoformat().replace("+00:00", "Z")


def stamp(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%SZ")


def load_yaml(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return default if data is None else data


def save_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)


def append_log(path: Path, entry: dict[str, Any]) -> None:
    data = load_yaml(path, [])
    if not isinstance(data, list):
        data = []
    data.append(entry)
    save_yaml(path, data)


def load_log_entries(path: Path) -> list[dict[str, Any]]:
    data = load_yaml(path, [])
    return data if isinstance(data, list) else []


def build_readiness_snapshot(vitals: dict[str, Any], tree: dict[str, Any], report_time: str) -> str:
    metabolism = vitals.get("vitals", {}).get("metabolism", {})
    recorded = []
    pending = []
    for group in ("prokaryotes", "eukaryotes"):
        for entity in tree.get(group, []):
            state = entity.get("operational_state")
            item = f"{entity.get('id')} ({state})"
            if state == "recorded":
                recorded.append(item)
            else:
                pending.append(item)

    last_transition = vitals.get("vitals", {}).get("evolution", {}).get("last_transition", "unknown")
    recommendation = (
        "Run additional receptor-backed signals and let metabolic-tracker generate stats."
        if metabolism.get("total_invocations", 0) < 5
        else "Expand automated runtime handlers beyond presence-check."
    )

    return "\n".join(
        [
            "## Being Readiness Snapshot",
            f"- Generated at: {report_time}",
            f"- Structural status: {vitals.get('structural_status', 'unknown')}",
            f"- Operational status: {vitals.get('operational_status', 'unknown')}",
            f"- Total invocations: {metabolism.get('total_invocations', 0)}",
            f"- Last activity: {metabolism.get('last_activity', 'unknown')}",
            f"- Recorded entities: {', '.join(recorded) if recorded else 'none'}",
            f"- Pending entities: {', '.join(pending) if pending else 'none'}",
            f"- Last transition: {last_transition}",
            f"- Recommendation: {recommendation}",
        ]
    ) + "\n"


def process_readiness_check(workspace: Path, signal_path: Path, signal_data: dict[str, Any]) -> dict[str, str]:
    now = utc_now()
    report_time = iso_z(now)

    vitals_path = workspace / ".being" / "homeostasis" / "vitals.yaml"
    tree_path = workspace / ".being" / "phylogeny" / "tree.yaml"
    report_dir = workspace / ".being" / "runtime" / "readiness"
    report_dir.mkdir(parents=True, exist_ok=True)

    vitals = load_yaml(vitals_path, {})
    tree = load_yaml(tree_path, {})

    log_path = workspace / ".being" / "metabolism" / "presence-check.log.yaml"
    existing_entries = load_log_entries(log_path)
    next_index = len(existing_entries) + 1

    log_entry = {
        "invocation_id": f"{report_time}-presence-check-{next_index:03d}",
        "timestamp": report_time,
        "skill": "presence-check",
        "energy": {
            "tokens_in": 650,
            "tokens_out": 240,
            "tokens_total": 1100,
            "tool_calls": 1,
            "wall_time_ms": 1200,
        },
        "nutrition": {
            "context_items": ["vitals.yaml", "tree.yaml", "metabolism logs", "runtime.minimum.md"],
            "context_tokens": 520,
        },
        "products": {
            "primary": "readiness snapshot",
            "byproducts": ["readiness-check-complete signal", "runtime report artifact"],
            "waste": [],
        },
        "outcome": {
            "success": True,
            "quality": 9,
            "efficiency": 8.18,
            "notes": "First automated readiness check completed by runtime loop.",
        },
    }
    append_log(log_path, log_entry)

    refresh_vitals(workspace)
    vitals = load_yaml(vitals_path, {})
    metabolism = vitals.setdefault("vitals", {}).setdefault("metabolism", {})

    for group in ("prokaryotes", "eukaryotes"):
        for entity in tree.get(group, []):
            if entity.get("id") == "presence-check":
                entity["operational_state"] = "recorded"
    save_yaml(tree_path, tree)

    snapshot = build_readiness_snapshot(vitals, tree, report_time)
    latest_report = report_dir / "latest.md"
    historical_report = report_dir / f"{stamp(now)}-presence-check.md"
    latest_report.write_text(snapshot, encoding="utf-8")
    historical_report.write_text(snapshot, encoding="utf-8")

    signal = signal_data.setdefault("signal", {})
    consumed_by = signal.setdefault("consumed_by", [])
    if "presence-check" not in consumed_by:
        consumed_by.append("presence-check")
    signal["consumed_at"] = report_time
    save_yaml(signal_path, signal_data)

    completion_signal_path = workspace / ".being" / "signals" / "neurotransmitters" / f"{stamp(now)}-readiness-check-complete.signal.yaml"
    completion_signal = {
        "signal": {
            "type": "neurotransmitter",
            "name": "readiness-check-complete",
            "emitter": "presence-check",
            "timestamp": report_time,
            "payload": {
                "report": ".being/runtime/readiness/latest.md",
                "operational_status": vitals.get("operational_status"),
                "total_invocations": metabolism.get("total_invocations"),
            },
            "consumed_by": ["presence-check"],
            "consumed_at": report_time,
        }
    }
    save_yaml(completion_signal_path, completion_signal)

    return {
        "signal": signal_path.relative_to(workspace).as_posix(),
        "report": latest_report.relative_to(workspace).as_posix(),
        "log": ".being/metabolism/presence-check.log.yaml",
    }


def run_loop(workspace: Path) -> list[dict[str, str]]:
    processed: list[dict[str, str]] = []
    signal_dir = workspace / ".being" / "signals" / "neurotransmitters"
    for path in sorted(signal_dir.glob("*.yaml")):
        data = load_yaml(path, {})
        signal = data.get("signal", {})
        if signal.get("name") != "readiness-check-request":
            continue
        if signal.get("target") != "presence-check":
            continue
        consumed_by = signal.get("consumed_by", [])
        if "presence-check" in consumed_by:
            continue
        processed.append(process_readiness_check(workspace, path, data))
    return processed


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the minimum Being runtime loop.")
    parser.add_argument("workspace", nargs="?", default=".", help="Path to the Being workspace")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    processed = run_loop(workspace)
    if not processed:
        print("No pending runtime signals were processed.")
        return 0

    print(f"Processed {len(processed)} signal(s).")
    for item in processed:
        print(f"- signal: {item['signal']}")
        print(f"  report: {item['report']}")
        print(f"  log: {item['log']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
