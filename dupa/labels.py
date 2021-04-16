"""Labels
A set of decorators that indicate if a function
has an unsolved bug in some case, might be not working,
or is not tested, maybe drafted.


If something is faulty, the person who knows it,
should mark this part of code accordingly, so that
that other person would know what to expect.

"""

from functools import wraps
import logging as log


DEPRECATED_MESSAGE = " DEPRECATED: Deprecated. Do not use"
DEPRECATING_MESSAGE = " DEPRECATING: Will be deprecated in the future"
FELER_MESSAGE = " FELER: Not working partially or enteirly"
NOT_TESTED_MESSAGE = " NOT TESTED: Function not tested"

def make_label_decorator(label):        
    def label_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            label()
            return func(*args, **kwargs)
        return wrap
    return label_decorator


"""
Regular labels that should be used to mark whole files
"""

def label_as_deprecated():
    log.warning(DEPRECATED_MESSAGE)

def label_as_deprecating():
    log.warning(DEPRECATING_MESSAGE)

def label_as_feler():
    log.warning(FELER_MESSAGE)

def label_as_not_tested():
    log.warning(NOT_TESTED_MESSAGE)
        

"""
Decorators that should mark functions and classes
"""

deprecated = make_label_decorator(label_as_deprecated)
deprecating = make_label_decorator(label_as_deprecating)
feler = make_label_decorator(label_as_feler)
not_tested = make_label_decorator(label_as_not_tested)
