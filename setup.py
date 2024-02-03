from setuptools import setup, find_packages

setup(
    name='kubectl-stash',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # your dependencies
    ],
    entry_points={
        'console_scripts': [
            'kubectlstash=kubectl_stash.cli:main',
        ],
    },
)
