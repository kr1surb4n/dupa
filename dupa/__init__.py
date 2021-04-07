# -*- coding: utf-8 -*-
"""Dupa"""  # noqa

__version__ = '0.0.1'
__author__ = 'Kris Urbanski <kris@whereibend.space>'


import time
from functools import wraps

"""timeit and debug are not mine."""

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(
            func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper

def debug(func):
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling:\n{func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned:\n{value!r}")
        print("\n")           # 4
        return value
    return wrapper_debug

def fixturize(func):
    """Create """
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling:\n{func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned:\n{value!r}")
        print("\n")           # 4
        return value
    return wrapper_debug



def print_wrap(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("Start: %s" % func.__name__)
        out = func(*args, **kwargs)
        print("End: %s" % func.__name__)
        return out
    return wrap

DUPA_COUNTER = 1

def dupa():
   global DUPA_COUNTER
   print(f"DUPA {DUPA_COUNTER}")
   DUPA_COUNTER += 1

def wysraj(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       dupa()
       return func(*args, **kwargs)
   return wrapps
   
def slow_down(func):
    """Sleep 1 second before calling the function"""
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down
