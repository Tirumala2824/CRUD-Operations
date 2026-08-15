# CRUD Operations

> A Python application for demonstrating create, read, update, and delete workflows across a small data-backed project with a Streamlit-facing entry point.

[![CI](https://github.com/Tirumala2824/CRUD-Operations/actions/workflows/ci.yml/badge.svg)](https://github.com/Tirumala2824/CRUD-Operations/actions/workflows/ci.yml)

## Status

**Category:** Application.

**Lifecycle:** Active remediation. The repository has a testable structure and CI baseline, but production deployment would require a reviewed persistence model, authentication and authorization, observability, migration strategy, and a validated deployment target.

## Features

The project demonstrates CRUD-oriented data access, application modules, a local database boundary, and a Streamlit-compatible interface. The tests protect repository structure and data contracts; feature behavior should be expanded with focused tests as the application boundary becomes more specific.

## Architecture

```text
Streamlit or application entry point
    -> modules and use-case functions
    -> database boundary
    -> persisted application data
```

Keep UI concerns, business rules, and persistence operations separate. Configuration belongs at the application boundary, and external input must be validated before it reaches the data layer. See [`docs/architecture.md`](docs/architecture.md) and [`docs/engineering-standards.md`](docs/engineering-standards.md).

## Local development

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Use the repository’s application entry point for local interaction. Before sharing a deployment command, verify the current `main.py`, `streamlit.py`, and database configuration in the target environment.

## Testing and quality

```bash
ruff check .
python -m compileall -q main.py modules tests
pytest -q
```

CI runs these checks on pushes to the default branch and on pull requests.

## Security and deployment limits

Never commit credentials, private data, or production databases. Before deployment, add explicit authentication, authorization, input validation, migration and backup procedures, error handling, logging, and a rollback path. This repository should not be treated as a production service until those boundaries are implemented and reviewed.

## Contributing and license

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), and [`CHANGELOG.md`](CHANGELOG.md). The repository is released under the MIT License; see [`LICENSE`](LICENSE).
