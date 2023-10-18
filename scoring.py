# Поставь себя на моё место

import sys
import json

scoring_filename = 'scoring.json'
with open(scoring_filename, 'r') as f:
    scoring_rules = json.load(f)

score = 0
test_group_index = 0
test_index = 0
for answer in sys.stdin:
    if answer == '\n':
        break
    answer = answer.strip()
    if answer == scoring_rules[test_group_index]['tests'][test_index]['pattern']:
        score += scoring_rules[test_group_index]['points'] // len(scoring_rules[test_group_index]['tests'])
    test_index += 1
    if test_index == len(scoring_rules[test_group_index]['tests']):
        test_index = 0
        test_group_index += 1

print(score)