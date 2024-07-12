#! /usr/bin/python3.12

import ctypes as ct 

libc = ct.CDLL('libc.so.6')
libc.printf(b"My name is %s\n", b"Fred")