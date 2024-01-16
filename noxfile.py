import os

import nox
from nox import options

PATH_TO_PROJECT = os.path.join(".", "TimeDB")
EXAMPLES_PATH = os.path.join(".", "examples")
SCRIPT_PATHS = [
    PATH_TO_PROJECT,
    EXAMPLES_PATH,
    "noxfile.py",
    os.path.join(".", "tests"),
]

options.sessions = ["format_fix", "pyright", "pytest", "docs"]


@nox.session()
def format_fix(session: nox.Session) -> None:
    session.install("-U", "ruff")
    session.run("python", "-m", "ruff", "format", *SCRIPT_PATHS)
    session.run("python", "-m", "ruff", *SCRIPT_PATHS, "--fix")


@nox.session()
def format(session: nox.Session) -> None:
    session.install("-U", "ruff")
    session.run("python", "-m", "ruff", "format", *SCRIPT_PATHS, "--check")
    session.run("python", "-m", "ruff", *SCRIPT_PATHS)


@nox.session()
def pyright(session: nox.Session) -> None:
    session.install(".")
    session.install("-U", "pyright")
    session.run("pyright", PATH_TO_PROJECT, EXAMPLES_PATH)


@nox.session()
def pytest(session: nox.Session) -> None:
    session.install(".")
    session.install("-U", "pytest")
    session.install("-U", "pytest-asyncio")
    session.run("pytest", "tests")


@nox.session()
def docs(session: nox.Session) -> None:
    session.install("-Ur", "doc_requirements.txt")
    session.install("-Ur", "requirements.txt")
    session.install("-U", "black")  # Signature formatting
    session.run("python", "-m", "mkdocs", "-q", "build")


@nox.session()
def servedocs(session: nox.Session) -> None:
    session.install("-Ur", "doc_requirements.txt")
    session.install("-Ur", "requirements.txt")
    session.install("-U", "black")  # Signature formatting
    session.run("python", "-m", "mkdocs", "serve")
