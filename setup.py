"""Setup data-structures module."""


from setuptools import setup

setup(
    name="data-structures",
    description="Python implementations of classic data structures",
    version=0.2,
    author=["Ford Fowler", "Claire Gatenby", "Casey O'Kane"],
    author_email=["fordjfowler@gmail.com",
                  'clairejgatenby@gmail.com',
                  "okanecasey@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list",
                "dll",
                "stack",
                'queue',
                'deque',
                'hashtable',
                'priority_queue',
                'bin_heap',
                'trie',
                'decision_tree',
                'k_means',
                'knn',
                ],
    install_requires=['numpy'],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox", 'numpy']
    }
)
