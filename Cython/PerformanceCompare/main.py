from utils import time_function
import regular_example
import use_cython_example

time_function("regular",regular_example.integrate_f,a=10,b=100,N=20)
time_function("Cython",use_cython_example.integrate_f,a=10,b=100,N=20)
