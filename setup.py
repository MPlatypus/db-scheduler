from setuptools import setup, find_namespace_packages
import typing as t


name = "db_scheduler"


def long_description() -> str:
    with open("README.md") as fp:
        return fp.read()


def parse_requirements_file(path: str) -> t.List[str]:
    with open(path) as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]


setup(
    name="db-scheduler",
    version="0.3.0",
    description="A voice library, for hikari.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="MPlaty",
    author_email="contact@mplaty.com",
    url="https://github.com/MPlatypus/db_scheduler",
    packages=find_namespace_packages(include=[name + "*"]),
    package_data={"db_scheduler": ["py.typed"]},
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_requirements_file("requirements.txt"),
    extras_require={
        "docs": parse_requirements_file("doc_requirements.txt"),
    },
    python_requires=">=3.11.0, <3.13",
    classifiers=[
        "Development Status :: 5 - Stable/Release",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.11",
    ],
)