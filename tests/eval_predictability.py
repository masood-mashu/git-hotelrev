"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitHotelRev.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.revpar_yield_calculator import *
from tools.dynamic_rate_optimizer import *
from tools.cancellation_buffer_estimator import *

class TestGitHotelRevPredictability(unittest.TestCase):
    def test_revpar_yield_calculator(self):
        res = calculate_revpar('{"adr_usd": 200.0, "occupancy_pct": 80.0}')
        self.assertEqual(res["revpar_usd"], 160.0)
        self.assertEqual(res["status"], "REVPAR_CALCULATED")

    def test_dynamic_rate_optimizer(self):
        res = optimize_room_rate('{"base_rate_usd": 100.0, "days_to_arrival": 7, "current_occupancy_pct": 85.0}')
        self.assertEqual(res["recommended_rate_usd"], 125.0)
        self.assertEqual(res["status"], "RATE_OPTIMIZED")

    def test_cancellation_buffer_estimator(self):
        res = estimate_cancellation_buffer('{"historical_no_show_pct": 5.0}')
        self.assertEqual(res["overbooking_buffer_pct"], 4.0)
        self.assertEqual(res["status"], "BUFFER_CALIBRATED")


if __name__ == "__main__":
    unittest.main()
