# data-science-mining-and-warehousing — tidy/repo-structure

This branch contains non-destructive repository organization changes and helper files to make the notebooks easier to run and to prepare the repo for a larger reorganization.

What I added on this branch

- `README.md` — this file (overview and next steps).
- `requirements.txt` — pinned packages used by the notebooks.
- `scripts/fix_notebook_paths.py` — a utility to replace absolute Colab paths (e.g. `/content/diabetes.csv`) with repo-relative `data/` paths inside notebooks (creates `.bak` backups).
- `docs/README.md` — guidance about lecture PDFs and recommended placement.

Why these changes

- The repo previously had no README or pinned dependencies; that makes it hard to reproduce the notebook environment during your datathon.
- The notebooks reference absolute paths (e.g. `/content/...`) that break outside Colab; the included script helps fix those to point to files inside a `data/` folder.

Next steps I recommend (manual or I can continue)

1. Move CSVs into a `data/` directory and (optionally) rename them to consistent names (e.g. `groceries.csv`, `diabetes.csv`).
   - Example local git commands:
     ```bash
     mkdir data
     git mv "Dataset 1.csv" data/groceries.csv
     git mv Dataset2.csv data/diabetes.csv
     git commit -m "chore(data): move CSVs into data/"
     ```
2. (Optional) I can continue on this branch and perform the moves + update notebooks in-place (creating `.bak` backups). If you'd like that, tell me to proceed and confirm the filename mapping (default mapping I suggest is in the README). Otherwise you can run the `fix_notebook_paths.py` script locally after moving files.

How to run the path-fixer (after moving CSVs)

```bash
python3 scripts/fix_notebook_paths.py
```

This will create `.bak` files for any notebook it modifies.

If you want me to continue and move files + update notebooks in this branch, reply and confirm the filename mapping (see below) or provide your preferred mapping.

Default filename mapping I would apply if you ask me to move files:
- `Dataset 1.csv` -> `data/groceries.csv`
- `Dataset2.csv` -> `data/diabetes.csv`
- `BostonHousing.csv` -> `data/boston_housing.csv`
- `employee_salary_data.csv` -> `data/employee_salary_data.csv`
- `Anova.csv` -> `data/Anova.csv` (kept same name)
- `penguins (2) (1).csv` -> `data/penguins.csv`

---

If you confirm the mapping I will continue and (1) create `data/` and move the CSVs there, (2) create `notebooks/` and move main notebooks there, and (3) update notebook paths and open a PR. If you'd rather run the moves locally, run the `git mv` commands above and then run the path-fixer script.
