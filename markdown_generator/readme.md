# Markdown Generator

These scripts convert structured source data into markdown files used by this site.

- `publications.py`: reads `publications.tsv` and writes paper entries into `_papers/`
- `pubsFromBib.py`: reads BibTeX files and writes paper entries into `_papers/`
- `talks.py`: reads `talks.tsv` and writes talk entries into `_talks/`
- `utils.py`: shared helpers for YAML front matter, escaping, and file output

The `.ipynb` notebooks are older exploratory versions of the same workflows. The `.py` scripts are the maintained command-line entry points.
