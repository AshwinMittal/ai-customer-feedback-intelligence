import unittest
from src.evaluate import evaluate

class EvalTests(unittest.TestCase):
    def test_perfect_answer(self):
        rows=[{'feedback_id':'F001','feedback':'The invoice price is unclear.'}]
        gold=[{'feedback_id':'F001','primary_theme':'billing_confusion'}]
        response={'classifications':[{'id':'F001','theme':'billing_confusion','evidence_quote':'invoice price'}], 'insights':[{'feedback_ids':['F001']}]} 
        result=evaluate(response,rows,gold)
        self.assertEqual(result['classification_accuracy'],1)
        self.assertFalse(result['unsupported_or_missing_quotes'])

    def test_invalid_quote(self):
        rows=[{'feedback_id':'F001','feedback':'The invoice price is unclear.'}]
        gold=[{'feedback_id':'F001','primary_theme':'billing_confusion'}]
        response={'classifications':[{'id':'F001','theme':'onboarding_setup','evidence_quote':'This never appeared'}], 'insights':[]}
        result=evaluate(response,rows,gold)
        self.assertEqual(result['classification_accuracy'],0)
        self.assertEqual(result['unsupported_or_missing_quotes'],['F001'])

if __name__ == '__main__':
    unittest.main()
