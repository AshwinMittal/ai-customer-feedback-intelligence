"""Offline, deterministic checks of LLM feedback-classification outputs."""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID_THEMES = {'onboarding_setup','notification_noise','reporting_visibility','billing_confusion','integration_sync','mobile_accessibility'}

def load_csv(path):
    with path.open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def evaluate(response, feedback_rows, gold_rows):
    feedback = {r['feedback_id']: r['feedback'] for r in feedback_rows}
    gold = {r['feedback_id']:r['primary_theme'] for r in gold_rows}
    classified = response.get('classifications', [])
    if not isinstance(classified,list):
        raise ValueError('classifications must be a list')
    ids = [r.get('id') for r in classified if isinstance(r,dict)]
    counts = Counter(ids)
    unique = {r['id']:r for r in classified if isinstance(r,dict) and isinstance(r.get('id'),str)}
    predicted_ids = set(unique)
    missing = sorted(set(gold) - predicted_ids)
    extra = sorted(predicted_ids - set(gold))
    duplicates = sorted(k for k,v in counts.items() if v>1 and isinstance(k,str))
    correct=0
    unknown_themes=[]
    bad_quotes=[]
    per_theme={theme:{'correct':0,'total':0} for theme in sorted(VALID_THEMES)}
    for ticket_id, true_theme in gold.items():
        per_theme[true_theme]['total']+=1
        item=unique.get(ticket_id)
        if not item:
            continue
        theme=item.get('theme')
        if theme not in VALID_THEMES:
            unknown_themes.append(ticket_id)
        if theme==true_theme:
            correct+=1
            per_theme[true_theme]['correct']+=1
        quote=item.get('evidence_quote','')
        if not isinstance(quote,str) or len(quote.strip())<5 or quote.lower() not in feedback[ticket_id].lower():
            bad_quotes.append(ticket_id)
    insights=response.get('insights',[])
    if not isinstance(insights,list):
        raise ValueError('insights must be a list')
    bad_insight_citations=[]
    for i,insight in enumerate(insights):
        ids_=insight.get('feedback_ids',[]) if isinstance(insight,dict) else []
        if not isinstance(ids_,list) or not ids_ or any(x not in feedback for x in ids_):
            bad_insight_citations.append(i)
    total=len(gold)
    return {
        'labeled_records':total,
        'covered_records':len(set(gold)&predicted_ids),
        'correct_classifications':correct,
        'classification_accuracy':round(correct/total,3),
        'invalid_ids':extra,
        'missing_ids':missing,
        'duplicate_ids':duplicates,
        'unknown_theme_ids':unknown_themes,
        'unsupported_or_missing_quotes':bad_quotes,
        'insights_with_invalid_or_missing_citations':bad_insight_citations,
        'per_theme':per_theme,
        'limitations':'A matching quotation or valid ID does not establish that an insight or recommendation is factually correct. Human review remains essential.'
    }

def main():
    parser=argparse.ArgumentParser(description='Evaluate feedback AI JSON output against local labels.')
    parser.add_argument('--input',required=True,help='Path to JSON output saved from an LLM')
    parser.add_argument('--report',help='Optional path to save evaluation metrics as JSON')
    args=parser.parse_args()
    result=json.loads(Path(args.input).read_text(encoding='utf-8'))
    report=evaluate(result,load_csv(ROOT/'data/feedback.csv'),load_csv(ROOT/'data/gold_labels.csv'))
    output=json.dumps(report,indent=2)
    print(output)
    if args.report:
        Path(args.report).parent.mkdir(parents=True,exist_ok=True)
        Path(args.report).write_text(output+'\n',encoding='utf-8')

if __name__=='__main__':
    main()
