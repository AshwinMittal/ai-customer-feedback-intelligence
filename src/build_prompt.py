"""Assemble a copy/paste prompt for ChatGPT. Uses Python standard library only."""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', choices=['v1', 'v2'], default='v1')
    args = parser.parse_args()
    with (ROOT / 'data/feedback.csv').open(encoding='utf-8', newline='') as f:
        dataset = list(csv.DictReader(f))
    template = (ROOT / f'prompts/{args.version}.md').read_text(encoding='utf-8')
    print(template.replace('{{FEEDBACK_ROWS}}', json.dumps(dataset, ensure_ascii=False, indent=2)))

if __name__ == '__main__':
    main()
