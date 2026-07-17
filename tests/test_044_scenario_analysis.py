import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck44(unittest.TestCase):
    def test_044_scenario_analysis(self):
        record = Record(id="segment-044", exposure=19745, signal=0.631, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
