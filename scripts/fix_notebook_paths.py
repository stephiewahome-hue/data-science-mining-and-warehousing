#!/usr/bin/env python3
"""
Replace common '/content/...' dataset paths in notebooks with repo-relative data/ filenames.
Creates a backup copy notebook.ipynb.bak before changing.
Adjust the mapping dict below if filenames differ.
"""
import json
from pathlib import Path

# mapping: match substring -> replacement
mapping = {
    "/content/diabetes.csv": "data/Dataset2.csv",
    "/content/Groceries_dataset.csv": "data/Dataset 1.csv",
    "/content/groceries_dataset.csv": "data/Dataset 1.csv",
}

# find notebooks in repo root and notebooks/ if present
nb_files = list(Path('.').glob('*.ipynb')) + list(Path('notebooks').glob('*.ipynb'))
changed = []

for nb_path in nb_files:
    text = nb_path.read_text(encoding='utf-8')
    new_text = text
    for old, new in mapping.items():
        if old in new_text:
            new_text = new_text.replace(old, new)
    if new_text != text:
        backup = nb_path.with_suffix(nb_path.suffix + '.bak')
        backup.write_text(text, encoding='utf-8')
        nb_path.write_text(new_text, encoding='utf-8')
        changed.append(str(nb_path))

print('Updated notebooks:', changed)
if not changed:
    print('No notebooks changed. Update mapping if your paths differ.')
