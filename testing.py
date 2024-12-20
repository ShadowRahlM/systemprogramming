#!/usr/bin/env python3
import numpy as np
import shutil,psutil
import csv


def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = np.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y


# print(numpyArray())

du = shutil.disk_usage('/')
usage = du.free/du.total*100
print(usage)

cpu = psutil.cpu_percent(1.5)
print(cpu)
