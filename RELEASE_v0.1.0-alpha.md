# Being v0.1.0-alpha

> First operational prototype

## Release summary

This is the first public version of Being that can reasonably be called an **operational prototype** rather than a purely conceptual system.

Being now includes:

- a protocol layer
- a runtime fact layer
- a validator
- a minimal runtime loop
- automatic vitals aggregation from metabolism logs

## What is included

### Protocols

The repository now contains a coherent minimum protocol stack for:

- membrane declaration
- metabolism logging
- signaling
- runtime minimum behavior
- phylogeny / manifest concepts

### First operational cycle

The repository records its first genuine execution loop and exposes it as repository fact instead of narrative only.

Key evidence includes:

- metabolism logs in [.being/metabolism/](.being/metabolism)
- phylogeny state in [tree.yaml](.being/phylogeny/tree.yaml)
- homeostasis state in [vitals.yaml](.being/homeostasis/vitals.yaml)
- validator output in [latest.validation.yaml](.being/validation/latest.validation.yaml)

### Minimal automation

Being now supports a minimal automated runtime handler for `readiness-check-request`, which can:

- consume a signal
- generate a readiness report
- write a new metabolism record
- refresh vitals from logs
- emit a completion signal

## Current status

This release should be read as:

- **research prototype**
- **operational MVP**
- **not yet a stable general-purpose framework**

## Recommended wording for GitHub release

## Being v0.1.0-alpha — first operational prototype

A protocol-driven computational organism prototype with:

- clean validation (`0 errors / 0 warnings`)
- first recorded operational cycle
- minimal runtime loop
- automatic vitals aggregation from runtime logs

## Next priorities

1. extend runtime handlers beyond `presence-check`
2. automate more signal-to-skill pathways
3. derive more state from facts instead of manual documents
4. prepare a future `being.yaml` publishing flow for ecosystem-level distribution
