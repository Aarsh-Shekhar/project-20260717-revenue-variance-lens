import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck59(unittest.TestCase):
    def test_059_reporting_view(self):
        record = Record(id="segment-059", exposure=78622, signal=0.631, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
