# RabTech Task 2 — Reproducible Research Project

This project implements the preregistered analysis using a **synthetic dataset**.

## Research question
Among college students, is greater weekly study time associated with a higher end-of-term exam score?

## Files
- `preregistration.md` — analysis plan created before examining outcome relationships.
- `data/raw/synthetic_students.csv` — synthetic fixture (100 rows).
- `src/analyze.py` — reproducible analysis pipeline.
- `tests/test_pipeline.py` — data-blind pipeline contract test.
- `requirements.lock` — pinned Python/package environment.
- `report/results.txt` — generated analysis output.

## Run
1. Create a Python 3.13 environment (or another compatible Python 3.x environment).
2. Install pinned packages:
   `pip install -r requirements.lock`
3. Run:
   `python src/analyze.py`
4. Run the pipeline test:
   `python -m unittest discover -s tests`

## Important
The dataset is synthetic and is included only to demonstrate that the pipeline works. It must not be presented as real survey/student evidence.
