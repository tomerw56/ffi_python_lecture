# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y build-essential python3-dev

# Install Cython
RUN pip install cython

# Create a working directory
WORKDIR /usr/src/app

# Copy the Cython and C++ source files to the container
COPY mymodule.pyx setup.py main.cpp ./

# Build the Cython module
RUN python setup.py build_ext --inplace


# Set the PYTHONPATH to the current directory
ENV PYTHONPATH=/usr/src/app

# Compile the C++ code
RUN g++ -o call_cython main.cpp -I/usr/include/python3.11 -lpython3.8 mymodule.cpython-38-x86_64-linux-gnu.so
RUN mv mymodule.cpython-38-x86_64-linux-gnu.so  mymodule.so
RUN ls
RUN ./call_cython
# Run the executable
CMD ["./call_cython"]