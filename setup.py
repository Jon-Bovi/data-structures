"""Setup data-structures module."""


from setuptools import setup


setup(
    name="data-structures",
    description="Python implementations of data structures.",
    version=0.3,
    author=["Ford Fowler",
            "Claire Gatenby",
            "Casey O'Kane",
            "Marc Kessler-Wenicker",
            "Sera Smith"],
    author_email=["fordjfowler@gmail.com",
                  'clairejgatenby@gmail.com',
                  "okanecasey@gmail.com",
                  "",
                  ""],
    licencse="MIT",
    packages=['data_structures'],
    package_dir={'data_structures': 'data_structures'},
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
