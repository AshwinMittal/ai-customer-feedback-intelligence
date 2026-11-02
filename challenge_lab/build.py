"""Challenge prompt builder. Run from the original repo root. No external dependencies."""
import argparse
import csv
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LAB = Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--version',choices=['v1','v2','v3'],required=True)
    args=parser.parse_args()
    template=(ROOT/'prompts'/f'{args.version}.md') if args.version in {'v1','v2'} else (LAB/'prompts/v3.md')
    if not template.exists():
        raise SystemExit('Expected this folder to be inside the original starter project alongside prompts/.')
    with (LAB/'data/challenge_feedback.csv').open(encoding='utf8',newline='') as f:
        rows=list(csv.DictReader(f))
    print(template.read_text(encoding='utf8').replace('{{FEEDBACK_ROWS}}',json.dumps(rows,indent=2,ensure_ascii=False)))
if __name__=='__main__':main()
