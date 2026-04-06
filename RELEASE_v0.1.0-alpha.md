# Being v0.1.0-alpha

> First operational prototype

## Release summary

`v0.1.0-alpha` is the first public version of Being that can reasonably be described as an operational prototype.

This repository is no longer only a conceptual design space. It now includes executable runtime behavior, recorded runtime facts, and a minimal validation path that makes the system inspectable from the outside.

## What Being is

Being is an experimental runtime for computational organisms.

It treats:

- skills as functional cells
- membranes as boundaries
- signals as coordination mechanisms
- metabolism as behavioral history
- phylogeny as evolutionary memory

## Highlights

- First recorded operational cycle
- Minimal runtime loop for `readiness-check-request`
- Clean validation state (`0 errors / 0 warnings`)
- Automatic vitals aggregation from metabolism logs

## What is included

### Protocol layer

The repository contains a coherent minimum protocol stack for:

- membrane declaration
- metabolism logging
- signaling
- runtime minimum behavior
- phylogeny and manifest concepts

### Runtime fact layer

Being now records observable runtime evidence, including:

- metabolism logs in [.being/metabolism/](.being/metabolism)
- phylogeny state in [tree.yaml](.being/phylogeny/tree.yaml)
- homeostasis state in [vitals.yaml](.being/homeostasis/vitals.yaml)
- validation state in [latest.validation.yaml](.being/validation/latest.validation.yaml)

### Minimal automation

The current runtime can already:

- consume a signal
- generate a readiness report
- write a metabolism record
- refresh vitals from runtime logs
- emit a completion signal

## Current status

This release should be understood as:

- a **research prototype**
- an **operational MVP**
- **not yet a stable general-purpose framework**

## Why this matters

The important shift in this release is not scale. It is evidence.

Being now has enough runtime structure to support validation, replay, and incremental evolution from facts rather than narrative alone.

## Next priorities

1. extend runtime handlers beyond `presence-check`
2. automate more signal-to-skill pathways
3. derive more state from facts instead of manual documents
4. prepare a future `being.yaml` publishing flow for ecosystem-level distribution
