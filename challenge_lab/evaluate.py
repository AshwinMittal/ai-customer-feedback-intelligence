"""Challenge evaluator: deterministic classification, review, and evidence checks."""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
LAB=Path(__file__).resolve().parent
LABELS={'onboarding_setup','notification_noise','reporting_visibility','billing_confusion','integration_sync','mobile_accessibility','needs_review'}

def load_rows(path):
    with Path(path).open(encoding='utf8',newline='') as f: return list(csv.DictReader(f))

def score(response, feedback_rows, gold_rows):
    if not isinstance(response,dict) or not isinstance(response.get('classifications'),list):
        raise ValueError('Expected JSON object containing classifications list')
    feedback={r['feedback_id']:r['feedback'] for r in feedback_rows}
    gold={r['feedback_id']:r['primary_theme'] for r in gold_rows}
    predictions=response['classifications']
    valid_entries=[r for r in predictions if isinstance(r,dict) and isinstance(r.get('id'),str)]
    ids=[r['id'] for r in valid_entries]
    counts=Counter(ids)
    by_id={r['id']:r for r in valid_entries}  # duplicates flagged below
    expected=set(gold)
    missing=sorted(expected-set(by_id))
    extras=sorted(set(by_id)-expected)
    duplicate=sorted(k for k,v in counts.items() if v>1)
    correct=0
    correct_active=0
    gold_active=0
    unknown=[]
    invalid_quotes=[]
    false_forced=[]
    unnecessary_review=[]
    predicted_review=0
    true_review=0
    per_theme=defaultdict(lambda:{'total':0,'correct':0})
    for rid, truth in gold.items():
        per_theme[truth]['total']+=1
        if truth=='needs_review':true_review+=1
        else:gold_active+=1
        item=by_id.get(rid)
        if not item:continue
        label=item.get('theme')
        if label not in LABELS:unknown.append(rid)
        if label=='needs_review':predicted_review+=1
        if label==truth:
            correct+=1;per_theme[truth]['correct']+=1
            if truth!='needs_review':correct_active+=1
        if truth=='needs_review' and label not in ('needs_review',None):false_forced.append(rid)
        if truth!='needs_review' and label=='needs_review':unnecessary_review.append(rid)
        quote=item.get('evidence_quote')
        if not isinstance(quote,str) or len(quote.strip())<5 or quote not in feedback[rid]:invalid_quotes.append(rid)
    insights=response.get('insights',[])
    if not isinstance(insights,list):raise ValueError('Expected insights list')
    bad_insight=[]
    for i,entry in enumerate(insights):
        refs=entry.get('feedback_ids') if isinstance(entry,dict) else None
        if not isinstance(refs,list) or not refs or any(r not in feedback for r in refs):bad_insight.append(i)
    total=len(gold)
    reviewed_correct=len([rid for rid in gold if gold[rid]=='needs_review' and by_id.get(rid,{}).get('theme')=='needs_review'])
    return {
      'total_records':total,
      'overall_accuracy':round(correct/total,3) if total else None,
      'non_review_classification_accuracy':round(correct_active/gold_active,3) if gold_active else None,
      'gold_review_cases':true_review,
      'predicted_review_cases':predicted_review,
      'review_recall':round(reviewed_correct/true_review,3) if true_review else None,
      'review_precision':round(reviewed_correct/predicted_review,3) if predicted_review else None,
      'forced_fit_errors':false_forced,
      'unnecessary_review_ids':unnecessary_review,
      'missing_ids':missing,
      'extra_ids':extras,
      'duplicate_ids':duplicate,
      'unknown_theme_ids':unknown,
      'unsupported_or_missing_quotes':invalid_quotes,
      'insights_with_invalid_or_missing_citations':bad_insight,
      'per_theme':dict(sorted(per_theme.items())),
      'caveats':'Synthetic annotated benchmark; gold is an adjudicated reference, not absolute truth. Substring checks cannot judge semantic support of insights. Changing prompt and allowed taxonomy at once is a product-policy change, not an isolated prompt A/B test.'
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--report')
    a=p.parse_args()
    data=json.loads(Path(a.input).read_text(encoding='utf8'))
    report=score(data,load_rows(LAB/'data/challenge_feedback.csv'),load_rows(LAB/'data/challenge_gold.csv'))
    rendered=json.dumps(report,indent=2)
    print(rendered)
    if a.report:
        out=Path(a.report)
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(rendered+'\n',encoding='utf8')
if __name__=='__main__':main()
