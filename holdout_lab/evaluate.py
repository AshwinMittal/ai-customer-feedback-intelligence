"""Reuse challenge_lab's verified scoring logic on the new holdout set."""
import argparse
import csv
import json
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
sys.path.insert(0, str(ROOT))
from challenge_lab.evaluate import score


def read_csv(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--report')
    args = parser.parse_args()
    predictions = json.loads(Path(args.input).read_text(encoding='utf-8'))
    feedback = read_csv(LAB / 'data/holdout_feedback.csv')
    gold = read_csv(LAB / 'data/holdout_gold.csv')
    report = score(predictions, feedback, gold)
    report['note'] = 'Curated synthetic holdout, not representative of real customer traffic. Both prompts use the same seven-theme taxonomy. Gold labels are authored, not independently adjudicated.'
    report_text = json.dumps(report, indent=2)
    print(report_text)
    if args.report:
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report_text + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
