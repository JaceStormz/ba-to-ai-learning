# ba-to-ai-learning

## Purpose
1–2 sentences: what this repo is (your BA→AI engineer learning repo, 105-week plan, Week 1 = environments + Git).

## Setup
1. `git clone https://github.com/JaceStormz/ba-to-ai-learning.git`
2. `cd ba-to-ai-learning`
3. `python -m venv .venv`
4. Activate — Git Bash: `source .venv/Scripts/activate` (PowerShell: `.venv\Scripts\Activate.ps1`)
5. `pip install -r requirements.txt`

## Week 1 — Lessons
Your five bullets, condensed: venv as isolated environment, Git as snapshots, why it matters, the BA connection, the risk.

## Mistakes & Fixes
The good stuff — this section is what makes a README worth reading:
- `deactivate` failing in a fresh shell → activation is per-shell, per-session
- requests 2.32.5 (system) vs 2.34.2 (venv) → the isolation lesson, on your own machine
- `.gitignore` needs no extension (not `.gitignore.py`)
- the `init.default` typo → the real key is `init.defaultBranch`

## Next Topics
Week 2: Python data structures and functions.