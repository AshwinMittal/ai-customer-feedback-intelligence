import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from evaluate import score
class ScoringTests(unittest.TestCase):
    def setUp(self):
        self.feedback=[{'feedback_id':'A','feedback':'All good.'},{'feedback_id':'B','feedback':'Duplicate emails every day.'}]
        self.gold=[{'feedback_id':'A','primary_theme':'needs_review'},{'feedback_id':'B','primary_theme':'notification_noise'}]
    def test_abstention(self):
        r={'classifications':[{'id':'A','theme':'needs_review','evidence_quote':'All good.'},{'id':'B','theme':'notification_noise','evidence_quote':'Duplicate emails'}],'insights':[]}
        out=score(r,self.feedback,self.gold)
        self.assertEqual(out['overall_accuracy'],1.0)
        self.assertEqual(out['review_recall'],1.0)
    def test_forced_fit_and_evidence(self):
        r={'classifications':[{'id':'A','theme':'billing_confusion','evidence_quote':'not in source'},{'id':'B','theme':'notification_noise','evidence_quote':'Duplicate emails'}],'insights':[]}
        out=score(r,self.feedback,self.gold)
        self.assertEqual(out['forced_fit_errors'],['A'])
        self.assertEqual(out['unsupported_or_missing_quotes'],['A'])
if __name__=='__main__':unittest.main()
