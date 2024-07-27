# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.rst", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("requirements-test.txt") as f:
    test_requirements = f.read().splitlines()
    test_requirements.remove("-r requirements.txt")

sync_requires = ["requests>=2.31,<3"]

async_requires = ["aiohttp>=3.8,<4"]

extras_require = {
    "sync": sync_requires,
    "async": async_requires,
    "full": sync_requires + async_requires,
}

setup(
    name="themoviedb",
    description="A modern and easy to use API wrapper for The Movie Database (TMDb) API v3 written in Python",
    long_description=readme,
    author="Leandro César",
    author_email="ccleandroc@gmail.com",
    url="https://github.com/leandcesar/themoviedb",
    version="1.0.2",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(include=["themoviedb", "themoviedb.*"]),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=[
        "tmdb",
        "tmdb3",
        "aiotmdb",
        "aiotmdb3",
        "themoviedb",
        "themoviedb3",
        "movie",
        "movies",
        "tv",
        "tv show",
        "tv shows",
    ],
    zip_safe=False,
    install_requires=requirements,
    extras_require=extras_require,
    tests_require=test_requirements,
    test_suite="tests",
)
