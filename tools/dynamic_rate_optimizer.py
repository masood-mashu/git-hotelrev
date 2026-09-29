"""
dynamic_rate_optimizer.py - Calculates dynamic rate recommendation based on remaining days and target occupancy
"""
import sys
import json


def optimize_room_rate(demand_json: str):
    import json
    data = json.loads(demand_json) if isinstance(demand_json, str) else demand_json
    base = data.get("base_rate_usd", 150.0)
    occ = data.get("current_occupancy_pct", 70.0)
    multiplier = 1.25 if occ > 80.0 else (1.10 if occ > 60.0 else 0.95)
    rec_rate = round(base * multiplier, 2)
    return {"recommended_rate_usd": rec_rate, "multiplier": multiplier, "status": "RATE_OPTIMIZED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dynamic-rate-optimizer"}))
