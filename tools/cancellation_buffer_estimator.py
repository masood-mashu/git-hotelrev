"""
cancellation_buffer_estimator.py - Calculates allowable overbooking buffer percentage based on historical no-show rate
"""
import sys
import json


def estimate_cancellation_buffer(cancellation_data_json: str):
    import json
    data = json.loads(cancellation_data_json) if isinstance(cancellation_data_json, str) else cancellation_data_json
    no_show = data.get("historical_no_show_pct", 5.0)
    buffer = min(round(no_show * 0.8, 1), 6.0)
    return {"overbooking_buffer_pct": buffer, "status": "BUFFER_CALIBRATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "cancellation-buffer-estimator"}))
