# Contributing

Thanks for your interest in contributing! Please follow these simple steps to ensure a smooth review process and maintain code quality.

## How to contribute
- Fork the repository and create a feature branch (use descriptive names).
- Make small, focused changes and open a Pull Request against `main`.
- Include tests that cover new behavior (see `tests/`).
- Run `pre-commit` hooks locally and ensure all checks pass:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pre-commit
pre-commit install
pre-commit run --all-files
pytest -q
```

## Code style
- Use `black` for formatting and `ruff` for linting. Pre-commit is configured to run these automatically.

## PR checklist
- [ ] Tests added/updated
- [ ] Linting passes
- [ ] All new code is type-annotated where applicable
- [ ] CI checks pass

## Testing & Coverage
- Add tests for new behavior and ensure coverage does not decrease for the project as measured by CI/Codecov.
- Aim for a **minimum overall coverage of 80%** (adjust as your team prefers). PRs that lower overall coverage may be asked to add tests to maintain baseline coverage.
- Run coverage locally:
```bash
# install coverage tooling
pip install pytest-cov

# run tests with coverage and see missing lines
pytest --cov=app --cov-report=term-missing -q

# produce XML report (used by CI/Codecov)
pytest --cov=app --cov-report=xml -q
```

## Questions
If you are unsure about a change, open an issue first so we can discuss the design.
