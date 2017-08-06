"""Setup data-structures module."""


from setuptools import setup

setup(
    name="data-structures",
    description="Python implementations of classic data structures",
    version=0.2,
    author=["Ford Fowler", "Casey O'Kane", "Claire Gatenby"],
    author_email=["fordjfowler@gmail.com",
                  "okanecasey@gmail.com",
                  'clairejgatenby@gmail.com'],
    licencse="MIT",
    packages=['data_structures'],
    package_dir={'data_structures': 'data_structures'},
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
