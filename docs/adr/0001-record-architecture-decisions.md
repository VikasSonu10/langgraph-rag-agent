# ADR 0001: Record Architecture Decisions

## Status
Accepted

## Context
As we walk through this curriculum (swapping frameworks, clouds, and
deployment patterns session by session), we will make decisions that
aren't obvious from the code alone — e.g. "why LangGraph first and not
Foundry" or "why Container Apps before AKS." Without a record, future
sessions (or a teammate) can't tell whether a design choice was
deliberate or incidental.

## Decision
We will use Architecture Decision Records (ADRs), stored in
`docs/adr/`, one file per decision, numbered sequentially. Each new
significant decision gets its own `NNNN-title.md` file using this same
template (Status / Context / Decision / Consequences).

## Consequences
- Every future session that changes framework, cloud, or deployment
  pattern should add a new ADR rather than silently overwriting this
  one.
- Keeps a running audit trail of *why*, not just *what*, which matters
  for a "production-grade" skeleton even at this early stage.
