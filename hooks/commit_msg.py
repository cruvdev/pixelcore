#!/usr/bin/env python
import re
import sys

# ==========================
# PIXELCORE COMMIT POLICY
# ==========================

PREFIXES = {
    "feat": "new feature",
    "fix": "bug fix",
    "docs": "documentation",
    "test": "tests",
    "chore": "maintenance tasks",
    "refactor": "refactoring code",
    "hotfix": "urgent production fix",
    "ci": "CI/CD workflow changes",
    "perf": "performance improvement",
    "build": "build / release changes",
}

MAX_SUBJECT_LENGTH = 72

PREFIX_PATTERN = re.compile(rf"^({'|'.join(PREFIXES.keys())}): [a-z].+")

# ==========================
# READ COMMIT MESSAGE
# ==========================

path = sys.argv[1]

with open(path, encoding="utf-8") as f:
    lines = f.readlines()

subject = None
for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    subject = line
    break

if subject is None:
    print("ERROR: Commit message is empty.")
    sys.exit(1)

# ==========================
# VALIDATION
# ==========================

if len(subject) > MAX_SUBJECT_LENGTH:
    print(f"ERROR: Commit subject exceeds {MAX_SUBJECT_LENGTH} characters.")
    print(f"Length: {len(subject)}")
    sys.exit(1)

if not PREFIX_PATTERN.match(subject):
    print("ERROR: Invalid commit message format.\n")
    print("Expected format:")
    print("  <prefix>: <short description>\n")
    print("Allowed prefixes:")
    for k, v in PREFIXES.items():
        print(f"  {k}: {v}")
    print("\nExample:")
    print("  build: bump version to 0.0.6")
    sys.exit(1)

# ==========================
# SUCCESS
# ==========================
sys.exit(0)
