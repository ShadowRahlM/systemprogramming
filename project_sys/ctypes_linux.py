#!/usr/bin/python3.12

import ctypes as ct 

# Load the C standard library
libc = ct.CDLL('libc.so.6')

# Set the argument types for the printf function
libc.printf.argtypes = [ct.c_char_p, ct.c_char_p]

# Set the return type for the printf function
libc.printf.restype = ct.c_int

# Variables to be used in the printf call
format_str = b"My name is %s\n"
name = b"Fred"

# Call the printf function
libc.printf(format_str, name)
