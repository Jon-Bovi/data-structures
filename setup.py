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
    package_dir={'': 'src'},
    py_modules=["linked_list", "stack", "dll", 'decision_tree', 'qqueue'],
    install_requires=['numpy'],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox", 'numpy']
    }
)
