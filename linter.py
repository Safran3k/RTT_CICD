import sys
from pylint import lint

THRESHHOLD = 10
run = lint.Run(["--rcfile.pylintrc", "main.py"], exit=False)
score = run.linter.stats.global_note

print(f"Score: {score}")

if score < THRESHHOLD:
    print(f"Linter failed, Score: {score} < threshhold")
    sys.exit(1)

sys.exit(0)