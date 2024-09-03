# Python Clean Architecture Boilerplate

[![GitHub license](https://img.shields.io/github/license/galezra/python-clean-architecture-boilerplate)](https://github.com/galezra/python-clean-architecture-boilerplate)

A robust Python boilerplate implementing clean architecture principles, with integrated tools for development, testing, and deployment.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [What's in the box ?](#whats-in-the-box-)
- [Clean Architecture](#clean-architecture)
- [Development Tools](#development-tools)
- [Testing](#testing)
- [Docker](#docker)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

- Python **>=3.12 <3.13** (tested with 3.12.5)
- [pre-commit](https://pre-commit.com/#install)
- [poetry](https://python-poetry.org/docs/#installation) **>=1.2.2 <1.9** (tested with 1.8.3)
- [docker](https://docs.docker.com/get-docker/) (optional)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/galezra/python-clean-architecture-boilerplate.git
   cd python-clean-architecture-boilerplate/
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

3. Set up pre-commit hooks:

   ```bash
   pre-commit install
   ```

---

## What's in the box ?

### Poetry

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. It allows you to
declare the libraries your project depends on and it will manage (install/update) them for you.

**pyproject.toml file** ([`pyproject.toml`](pyproject.toml)): orchestrate your project and its dependencies
**poetry.lock file** ([`poetry.lock`](poetry.lock)): ensure that the package versions are consistent for everyone
working on your project

For more configuration options and details, see the [configuration docs](https://python-poetry.org/docs/).

### pre-commit

[pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks.

**.pre-commit-config.yaml file** ([`.pre-commit-config.yaml`](.pre-commit-config.yaml)): describes what repositories and
hooks are installed

For more configuration options and details, see the [configuration docs](https://pre-commit.com/).

### ruff

[ruff](https://github.com/charliermarsh/ruff) is an extremely fast Python linter, written in Rust.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://github.com/charliermarsh/ruff#configuration).

### mypy

[mypy](http://mypy-lang.org/) is an optional static type checker for Python that aims to combine the benefits of
dynamic (or "duck") typing and static typing.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://mypy.readthedocs.io/).

### bandit

[bandit](https://bandit.readthedocs.io/) is a tool designed to find common security issues in Python code.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://bandit.readthedocs.io/).

### docformatter

[docformatter](https://github.com/PyCQA/docformatter) is a tool designed to format docstrings to
follow [PEP 257](https://peps.python.org/pep-0257/).

Options are defined in the [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

---

## Clean Architecture

This boilerplate follows the principles of Clean Architecture, which promotes separation of concerns and independence of frameworks. The project structure is organized into layers:

1. **Domain Layer**: Contains business logic and entities.
2. **Use Case Layer**: Implements application-specific business rules.
3. **Interface Adapters**: Converts data between the use cases and external agencies.
4. **Frameworks and Drivers**: Contains frameworks and tools like databases, web frameworks, etc.

Benefits of this architecture:

- **Testability**: Business logic can be tested independently of the UI, database, or any external element.
- **Independence of Framework**: The architecture doesn't depend on the existence of some library of feature-laden software.
- **Independence of UI**: The UI can change easily, without changing the rest of the system.
- **Independence of Database**: You can swap out databases without affecting the business rules.

The `src/` directory is structured to reflect these layers, promoting a clear separation of concerns and making the codebase more maintainable and scalable.

---

## Development Tools

This boilerplate includes several development tools to ensure code quality and consistency:

- **Poetry**: Dependency management and packaging
- **pre-commit**: Multi-language pre-commit hook framework
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checker
- **bandit**: Security issue finder
- **docformatter**: Docstring formatter
- **pytest**: Testing framework

For detailed configurations, refer to `pyproject.toml` and `.pre-commit-config.yaml`.

---

## Testing

Run tests using pytest:

```bash
poetry run pytest tests
```

For coverage report:

```bash
poetry run pytest tests --cov=src
```

---

## Docker

Build the Docker image:

```bash
docker build . -t my-python-application:latest
```

Run the application in Docker:

```bash
docker run -p 8000:8000 -it --rm my-python-application:latest
```

---

## Configuration

The application uses YAML configuration files located in the `config/` directory. The `ENVIRONMENT` environment variable determines which configuration file to use:

- `config/default.yaml`: Default configuration
- `config/staging.yaml`: Staging environment configuration
- `config/production.yaml`: Production environment configuration

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
