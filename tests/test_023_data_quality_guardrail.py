import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck23(unittest.TestCase):
    def test_023_data_quality_guardrail(self):
        record = Record(id="segment-023", exposure=18591, signal=0.565, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
