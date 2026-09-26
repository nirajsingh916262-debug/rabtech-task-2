import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analyze import load_and_validate

class TestPipelineContract(unittest.TestCase):
    def test_synthetic_fixture_contract(self):
        df = load_and_validate()
        self.assertEqual(len(df), 100)
        self.assertEqual(
            list(df.columns),
            ["student_id", "study_hours_per_week", "sleep_hours_per_night", "exam_score"]
        )
        self.assertTrue(df["student_id"].is_unique)
        self.assertTrue(df["exam_score"].between(0, 100).all())

if __name__ == "__main__":
    unittest.main()
