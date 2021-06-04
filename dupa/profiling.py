#!/usr/bin/env python
# -*- coding: utf-8 -*-

# I dont know where that came from. This code is not mine.
# Anyway, it's awesome.

from cProfile import Profile
from functools import wraps
import pstats
import pyprof2calltree

profiler = Profile()


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        func_return_value = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(
            func.__module__, func.__name__, end - start))
        return func_return_value
    return wrapper


def slow_down(func):
    """Sleep 1 second before calling the function"""
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


def profile(cumulative=True, print_stats=0, sort_stats='cumulative',
            dump_stats=False, profile_filename='profilestats.out',
            callgrind_filename='callgrind.out'):
    def closure(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            result = None
            if cumulative:
                global profiler
            else:
                profiler = Profile()
            try:
                result = profiler.runcall(func, *args, **kwargs)
            finally:
                if dump_stats:
                    profiler.dump_stats(profile_filename)
                stats = pstats.Stats(profiler)
                conv = pyprof2calltree.CalltreeConverter(stats)
                with open(callgrind_filename, 'w') as fd:
                    conv.output(fd)
                if print_stats:
                    stats.strip_dirs().sort_stats(
                        sort_stats).print_stats(print_stats)
            return result
        return decorator
    return closure
