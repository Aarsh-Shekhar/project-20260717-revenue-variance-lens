import unittest

from revenue_variance_lens.models import Record
from revenue_variance_lens.scoring import score_record


class DepthCheck47(unittest.TestCase):
    def test_047_control_mapping(self):
        record = Record(id="segment-047", exposure=9922, signal=0.439, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
