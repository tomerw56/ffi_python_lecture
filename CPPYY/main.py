import cppyy

# Load the C++ header
cppyy.include('myclass.h')

# If necessary, provide the class definition again (or ensure it is loaded only once)
cppyy.cppdef("""
#include "myclass.h"
""")

# Create an instance of the C++ class
my_obj = cppyy.gbl.MyClass(10)

# Call methods on the C++ object
print("Initial value:", my_obj.get_value())  # Should print: Initial value: 10

my_obj.set_value(42)
print("Updated value:", my_obj.get_value())  # Should print: Updated value: 42
