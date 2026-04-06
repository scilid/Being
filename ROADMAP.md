# Roadmap

> Public roadmap for the evolution of Being after `v0.1.0-alpha`

Being is still an experimental runtime for computational organisms.

This roadmap does not promise fixed delivery dates. It describes the next layers of capability the repository is expected to grow into.

---

## Current release: `v0.1.0-alpha`

What already exists:

- a protocol layer
- a runtime fact layer
- a minimal validator
- a minimal runtime loop
- automatic vitals aggregation from metabolism logs
- the first recorded operational cycle

This is the baseline from which future versions will evolve.

---

## Phase 1 — stabilize the operational prototype

### Target outcomes

- keep validation consistently clean
- reduce manual state updates
- strengthen runtime fact generation
- improve public documentation for new visitors

### Candidate work

- expand `presence-check` reporting
- make more state derive from runtime facts
- improve validator coverage for protocol drift
- document canonical file and signal conventions more clearly

---

## Phase 2 — broaden signal-to-skill execution

### Target outcomes

- support more than one automated pathway
- make signal handling less special-cased
- increase replayability of runtime events

### Candidate work

- extend runtime handlers beyond `readiness-check-request`
- support additional receptors and dispatch rules
- formalize signal consumption and completion semantics
- improve traceability between signals, receptors, and metabolism logs

---

## Phase 3 — strengthen organism identity and memory

### Target outcomes

- make global state more evidence-driven
- enrich phylogeny and homeostasis as runtime truth sources
- reduce narrative-only state claims

### Candidate work

- derive more of `.being/homeostasis/vitals.yaml` from logs and reports
- formalize evolution checkpoints in `.being/phylogeny/tree.yaml`
- add stronger consistency checks across truth sources
- improve replay and audit narratives from recorded facts

---

## Phase 4 — prepare ecosystem publication

### Target outcomes

- define how a Being can be shared, imported, or reproduced
- make repository structure easier for external contributors to understand
- prepare for a future ecosystem-level publishing model

### Candidate work

- design a future `being.yaml` publishing format
- define import/export expectations for organisms and skills
- improve contributor-facing templates and repository onboarding
- clarify the relationship between Being, skills, membranes, and biosphere concepts

---

## Near-term public priorities

If someone lands on this repository today, the most important next wins are:

1. more automated runtime pathways
2. more state derived from facts
3. clearer contributor entry points
4. stronger release-quality documentation

---

## Status note

This roadmap should be read as directional, not contractual.

Being is evolving as a research prototype, so priorities may shift as the runtime becomes more observable and more executable.
