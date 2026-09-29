# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitHotelRev** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitHotelRev Automation Engine`
* **Responsibilities**:
  * Computes daily ADR, RevPAR, and occupancy yield indices across room category inventories.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitHotelRev Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies competitor rate shop data and checks minimum stay restrictions (LOS).
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Director of Revenue Management / Hotel General Manager (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
