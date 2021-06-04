# -*- coding: utf-8 -*-
"""Dupa

Set of tools handy during working, debuging and testing
the code."""

__version__ = '0.0.1'
__author__ = 'Kris Urbanski <kris@whereibend.space>'


import time
from functools import wraps
from dupa.fixturize import fixturize

def debug(func):
    """Print the function signature and return value"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Signature:\n{func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__} RETURN:\n{value!r}\n")

        return value
    return wrapper_debug

def print_wrap(func):
    @wraps(func)
    def wrap(*args, **kwargs):

        print("DUPA Start: %s" % func.__name__)

        out = func(*args, **kwargs)

        print("DUPA End: %s" % func.__name__)

        return out
    return wrap

DUPA_COUNTER = 1

def _kupa_(marker=None):
    global DUPA_COUNTER
    
    print(f"DUPA {marker if marker else DUPA_COUNTER}")

    if not marker:
        DUPA_COUNTER += 1


def dupa(marker=None):
    def closure(func):
        """A decorator around a function."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            _kupa_(marker)
            return func(*args, **kwargs)
        return wrapper
    return closure


