# setup.py
# compile with ../venv39/bin/python3.9 setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
setup(
    ext_modules=cythonize(
        "issues.pyx"
    )
)
