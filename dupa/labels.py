"""Labels
A set of decorators that indicate if a function
has an unsolved bug in some case, might be not working,
or is not tested, drafted"""

from functools import wraps
import logging as log
import warnings


def make_label_decorator(label):        
    def label_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            label()
            return func(*args, **kwargs)
        return wrap
    return label_decorator


def label_as_deprecated():
    log.warning(" DEPRECATED: Deprecated. Do not use")

def label_as_deprecating():
    log.warning(" DEPRECATING: Will be deprecated in the future")

def label_as_feler():
    log.warning(" FELER: Not working partially or enteirly")

def label_as_not_tested():
    log.warning(" NOT TESTED: Function not tested")
        

deprecated = make_label_decorator(label_as_deprecated)
deprecating = make_label_decorator(label_as_deprecating)
feler = make_label_decorator(label_as_feler)
not_tested = make_label_decorator(label_as_not_tested)
