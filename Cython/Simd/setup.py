# setup.py
# compile with: CFLAGS="-O3" ../venv39/bin/python3.9 setup_numpy.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
import numpy
Cython.Compiler.Options.annotate = True

setup(
    ext_modules=cythonize(
        "simd_example.pyx", annotate=True,
    ),
    include_dirs=[numpy.get_include()],
)