#!/usr/bin/env python

import sys
import os
import psutil

def ordinary(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError("Wrong number of arguments")
        for line in ordinary(sys.argv[1]):
            pass
        process = psutil.Process(os.getpid())
        print(f'Peak memory usage = {process.memory_info().rss / 1024 ** 3:0.3f} GB')
        cpu_times = process.cpu_times()
        print(f'User Mode Time + System Mode Time = {cpu_times.user + cpu_times.system:0.2f}s')
    except ValueError as err:
        print('\033[91mException!', err)
    except FileNotFoundError as err:
        print('\033[91mException!', err)

# /goinfre/agidget/day04/ratings.csv
