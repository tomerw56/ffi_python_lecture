# setup.py
# compile with ../venv39/bin/python3.9 setup_numpy.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
import numpy
Cython.Compiler.Options.annotate = True


setup(
    ext_modules=cythonize(
        "solution_cython_numpy.pyx", compiler_directives={"language_level": "3"}, annotate=True
    ),
    include_dirs=[numpy.get_include()],
)