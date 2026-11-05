"""Build v3 or v4 prompts for the holdout data without loading any gold labels."""
import argparse
import csv
import json
from pathlib import Path

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True, choices=['v3','v4'])
    args = parser.parse_args()
    template = ROOT / 'challenge_lab/prompts/v3.md' if args.version == 'v3' else LAB / 'prompts/v4.md'
    if not template.exists():
        raise SystemExit('Copy holdout_lab alongside the existing challenge_lab directory in the original project.')
    with (LAB / 'data/holdout_feedback.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    print(template.read_text(encoding='utf-8').replace('{{FEEDBACK_ROWS}}', json.dumps(rows, indent=2, ensure_ascii=False)))

if __name__ == '__main__':
    main()
