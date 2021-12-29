#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Joao Filho Drummer",
    author_email="devdrummerzzz@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Faz a validação de CPF e CNPJ Brasileiro",
    entry_points={"console_scripts": ["brtools=brtools.cli:main",],},
    install_requires=[
        "validate-cpf==0.1.2",
        "validate-cnpj==0.0.1"
    ],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"brtools": ["py.typed"]},
    include_package_data=True,
    keywords="brtools",
    name="python-brtools",
    package_dir={"": "src"},
    packages=find_packages(include=["src/brtools", "src/brtools.*"]),
    setup_requires=[],
    url="https://github.com/drummerzzz/pypi_brtools",
    version="0.0.2",
    zip_safe=False,
)
