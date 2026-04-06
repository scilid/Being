# Changelog

All notable changes to this project will be documented in this file.

The format is loosely based on Keep a Changelog and follows semantic versioning at the release-label level appropriate for an experimental prototype.

## [v0.1.0-alpha] - 2026-04-06

### Added

- Root project entrypoint [README.md](README.md)
- Minimum runtime specification in [runtime.minimum.md](protocols/runtime.minimum.md)
- Protocol consistency audit in [001-protocol-consistency-audit.md](lab/audits/001-protocol-consistency-audit.md)
- First operational field note in [005-first-operational-cycle.md](lab/field-notes/005-first-operational-cycle.md)
- New native Skill `presence-check`
- Runtime validator in [validator.py](runtime/validator.py)
- Runtime loop in [loop.py](runtime/loop.py)
- Vitals aggregation logic in [aggregation.py](runtime/aggregation.py)
- Manual vitals aggregation entrypoint in [aggregate_vitals.py](runtime/aggregate_vitals.py)
- Validation report output in [.being/validation/](.being/validation)
- Runtime readiness reports in [.being/runtime/readiness/](.being/runtime/readiness)

### Changed

- Unified signal naming around `kebab-case`
- Migrated membrane files to directory-style paths under `organisms/{grade}/{skill}/{skill}.membrane.yaml`
- Split phylogeny state into `evolutionary_grade`, `symbiotic_status`, and `operational_state`
- Changed `vitals.yaml` from manually narrated state toward log-derived state
- Elevated Being from `not-yet-alive` to `operationally-alive` based on recorded execution evidence

### Fixed

- Removed protocol inconsistencies that prevented clean validation
- Eliminated validator errors and warnings for the current workspace state
- Aligned receptor declarations with membrane signal contracts
- Corrected signal chronology for automated readiness checks

### Notes

This release is an experimental prototype, not a stable framework API.
