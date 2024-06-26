from setuptools import setup, find_packages


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()


def read_file(file):
    with open(file) as f:
        return f.read()


version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name='quant-common',
    version=version,
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    author='dalcon10028',
    author_email='dalcon10280@gmail.com',
    install_requires=requirements,
)
