from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


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


def _parse_timestamp(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def collect_metabolism_stats(workspace: Path) -> dict[str, Any]:
    metabolism_dir = workspace / ".being" / "metabolism"
    total_invocations = 0
    total_tokens = 0
    efficiency_values: list[float] = []
    last_activity: str | None = None
    last_activity_dt: datetime | None = None

    for path in sorted(metabolism_dir.glob("*.log.yaml")):
        data = load_yaml(path, [])
        if not isinstance(data, list):
            continue
        for item in data:
            total_invocations += 1
            energy = item.get("energy", {})
            tokens_total = energy.get("tokens_total", 0)
            if isinstance(tokens_total, (int, float)):
                total_tokens += int(tokens_total)

            outcome = item.get("outcome", {})
            efficiency = outcome.get("efficiency")
            if isinstance(efficiency, (int, float)):
                efficiency_values.append(float(efficiency))

            timestamp = item.get("timestamp")
            dt = _parse_timestamp(timestamp)
            if dt and (last_activity_dt is None or dt > last_activity_dt):
                last_activity_dt = dt
                last_activity = timestamp

    average_efficiency = None
    if efficiency_values:
        average_efficiency = round(sum(efficiency_values) / len(efficiency_values), 2)

    return {
        "total_invocations": total_invocations,
        "total_tokens_consumed": total_tokens,
        "average_efficiency": average_efficiency,
        "last_activity": last_activity,
    }


def refresh_vitals(workspace: Path) -> dict[str, Any]:
    vitals_path = workspace / ".being" / "homeostasis" / "vitals.yaml"
    vitals = load_yaml(vitals_path, {})
    metabolism = vitals.setdefault("vitals", {}).setdefault("metabolism", {})
    stats = collect_metabolism_stats(workspace)
    metabolism.update(stats)

    if stats["total_invocations"] > 0:
        vitals["operational_status"] = "operationally-alive"
    else:
        vitals["operational_status"] = "not-yet-alive"

    save_yaml(vitals_path, vitals)
    return stats
