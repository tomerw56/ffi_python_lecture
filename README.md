# ffi_python_lecture
the content for the lecture https://docs.google.com/presentation/d/15NT43vujrvG7cbrnbFsAau3SeKaZ8Sb-YwNtpMnHS9Q/edit?usp=sharing

# disclaimer
These examples are taken from code snipets provided via links on the lecture - i take no credit for them! 
I will try to provide the most accurate links in them-if you have found any error in the credits please let me know.

# Environment
I used my ubuntu laptop, no special hw needed.
1. For rust you do need the rust installations.
2. my venv included **cython,numpy,rustimport,cppyy,numba**
3. the examples were tested on python 3.9
4. PyBind11 sample needs pybind11 - see the cmake file
5. Some exampels are docker based so you need that support as well
6. Please notre that some cython and cpp examples code are in seperated folders and need to be build.
7. The CPP code in 
4. I tried to add to every compiled file the compilation instructions.
# The Credits
1. ChatGPT helped obviously.
2. The https://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/ provided me the py03 example
2. I heavily used https://pythonspeed.com
3. Cpp - swig https://gist.github.com/mattbierbaum/1193397
4. SimpleCppToPython - https://pythonspeed.com/articles/rust-cython-python-extensions/
5. NUMBA - 
   1.    https://pythonspeed.com/articles/slow-numba/
2. pybind11 - https://pybind11.readthedocs.io/en/stable/advanced/embedding.html -
3. Rust
   1. https://pythonspeed.com/articles/vectorization-python/
   4. https://pythonspeed.com/articles/easiest-rust-python/
   5.  https://pythonspeed.com/articles/rust-cython-python-extensions/
6. Cython - a lot of help
   7. https://www.peterbaumgartner.com/blog/intro-to-just-enough-cython-to-be-useful/
   8. https://pythonspeed.com/articles/faster-cython-simd/


