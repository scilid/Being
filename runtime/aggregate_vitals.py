from __future__ import annotations

import argparse
from pathlib import Path

from aggregation import refresh_vitals


def main() -> int:
    parser = argparse.ArgumentParser(description="Aggregate Being vitals from metabolism logs.")
    parser.add_argument("workspace", nargs="?", default=".", help="Path to the Being workspace")
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    stats = refresh_vitals(workspace)
    print("Vitals refreshed from metabolism logs.")
    print(f"- total_invocations: {stats['total_invocations']}")
    print(f"- total_tokens_consumed: {stats['total_tokens_consumed']}")
    print(f"- average_efficiency: {stats['average_efficiency']}")
    print(f"- last_activity: {stats['last_activity']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
