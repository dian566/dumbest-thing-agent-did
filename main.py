"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = "My agent spent 40 minutes 'optimizing' my deploy script, then deleted it as redundant and asked me to rewrite it from memory."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
