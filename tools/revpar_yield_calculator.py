"""
revpar_yield_calculator.py - Computes RevPAR from Average Daily Rate (ADR) and Occupancy percentage
"""
import sys
import json


def calculate_revpar(pms_metrics_json: str):
    import json
    data = json.loads(pms_metrics_json) if isinstance(pms_metrics_json, str) else pms_metrics_json
    adr = data.get("adr_usd", 180.0)
    occ = data.get("occupancy_pct", 85.0)
    revpar = round(adr * (occ / 100.0), 2)
    return {"revpar_usd": revpar, "adr_usd": adr, "occupancy_pct": occ, "status": "REVPAR_CALCULATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "revpar-yield-calculator"}))
