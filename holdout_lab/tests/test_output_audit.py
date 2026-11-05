import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_outputs import audit

class OutputAuditTests(unittest.TestCase):
    def setUp(self):
        self.feedback = {f'H{i}':f'Example Feedback {i}' for i in range(1,7)}
        self.classifications = [{'id':f'H{i}','theme':'integration_sync', 'evidence_quote':f'Example Feedback {i}'} for i in range(1,7)]

    def test_detects_extra_insight(self):
        d={'classifications':self.classifications, 'insights':[{'theme':'integration_sync','feedback_ids':['H1']}] * 6}
        self.assertFalse(audit(d, self.feedback)['insight_count_contract_pass'])

    def test_detects_case_sensitive_quote_failure(self):
        d={'classifications':list(self.classifications),'insights':[]}
        d['classifications'][0]=dict(d['classifications'][0],evidence_quote='example Feedback 1')
        self.assertIn('H1',audit(d,self.feedback)['exact_quote_failures'])

    def test_identifies_missing_theme_summary(self):
        d={'classifications':list(self.classifications),'insights':[]}
        self.assertEqual(audit(d,self.feedback)['active_themes_without_insight'], ['integration_sync'])

if __name__=='__main__':unittest.main()
