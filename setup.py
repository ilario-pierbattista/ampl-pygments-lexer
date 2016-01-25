import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
        name="ampl-pygments-lexer",
        version="0.0.2",
        author="Ilario Pierbattista",
        author_email="pierbattista.ilario@gmail.com",
        description="An AMPL language lexer for pygments",
        license="BSD",
        keywords="AMPL lexer pygments",
        packages=find_packages(),
        install_requires=[
            "pygments"
        ],
        entry_points="""[pygments.lexers]
                        ampl=ampl_pygments_lexer:AmplLexer"""
)
