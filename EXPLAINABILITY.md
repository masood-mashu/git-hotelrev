# Explainability, Auditability & Decision Logic: GitHotelRev

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitHotelRev**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitHotelRev** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Property**: Property Management System (PMS) reservation logs and room inventory status.
- **Historical**: Historical occupancy curves and lead-time booking pace statistics.
- **Local**: Local event calendars and competitive set (CompSet) daily rate feeds.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **calculate_revpar**: Uses `revpar-yield-calculator` to calculate computes revpar from average daily rate (adr) and occupancy percentage.
   - **optimize_room_rate**: Uses `dynamic-rate-optimizer` to calculate calculates dynamic rate recommendation based on remaining days and target occupancy.
   - **estimate_cancellation_buffer**: Uses `cancellation-buffer-estimator` to calculate calculates allowable overbooking buffer percentage based on historical no-show rate.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When daily property revenue metrics are ingested, the agent executes revpar_yield_calculator, dynamic_rate_optimizer, and cancellation_buffer_estimator. If RevPAR index outperforms CompSet and rates adhere to policy, it issues APPROVED. If compression periods require minimum-stay rules, it issues NEEDS_REVIEW. If rate drops below brand preservation floor, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on STR hospitality metrics.
- **Requires**: Requires accurate PMS out-of-order room status to prevent false capacity reporting.
- **Does**: Does not alter contracted corporate negotiated rates without corporate sales authorization.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
