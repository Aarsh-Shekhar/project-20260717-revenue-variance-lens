import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck53(unittest.TestCase):
    def test_053_data_quality_guardrail(self):
        record = Record(id="segment-053", exposure=76176, signal=0.212, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
