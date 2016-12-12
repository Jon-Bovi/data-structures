"""Setup data-structures module."""


from setuptools import setup

setup(
    name="data-structures",
    description="Python implementations of classic data structures",
    version=0.1,
    author=["Ford Fowler", "Casey O'Kane"],
    author_email=["fordjfowler@gmail.com", "okanecasey@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
