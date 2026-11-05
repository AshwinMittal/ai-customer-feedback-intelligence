import csv
import unittest
from pathlib import Path
LAB = Path(__file__).resolve().parents[1]
VALID = {'onboarding_setup','notification_noise','reporting_visibility','billing_confusion','integration_sync','mobile_accessibility','needs_review'}

class HoldoutDataTests(unittest.TestCase):
    def test_ids_unique_and_labels_valid(self):
        with (LAB / 'data/holdout_feedback.csv').open(newline='', encoding='utf-8') as f:
            rows = list(csv.DictReader(f))
        with (LAB / 'data/holdout_gold.csv').open(newline='', encoding='utf-8') as f:
            labels = list(csv.DictReader(f))
        self.assertEqual(len(rows), 36)
        self.assertEqual(len({r['feedback_id'] for r in rows}), 36)
        self.assertEqual({r['feedback_id'] for r in rows}, {r['feedback_id'] for r in labels})
        self.assertTrue(all(r['primary_theme'] in VALID for r in labels))
        self.assertTrue(all(r['feedback'].strip() for r in rows))

    def test_v4_taxonomy_and_schema(self):
        text = (LAB / 'prompts/v4.md').read_text()
        self.assertTrue(all(k in text for k in VALID))
        self.assertIn('evidence_quote', text)

if __name__ == '__main__':
    unittest.main()
