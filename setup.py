import tomli
from setuptools import setup


def get_requirements():
    try:
        pipfile = tomli.loads(open("Pipfile").read())
    except FileNotFoundError:
        return []
    try:
        pkgs = pipfile["packages"].items()
    except KeyError:
        return []
    return [f"{pkg}{ver}" if ver != "*" else pkg for pkg, ver in pkgs]


setup(
    name="treasure",
    version="0.0.1",
    packages=["treasure"],
    install_requires=get_requirements(),
)
