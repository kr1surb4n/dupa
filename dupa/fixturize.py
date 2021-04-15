from functools import wraps


def fixturize(func):
    """Create"""
    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        value = func(*args, **kwargs)

        with open(f"debug__{func.__name__}__call.fix", 'w+') as file:
            file.write(f"{func.__name__}({signature})")
        
        with open(f"debug__{func.__name__}__return.fix", 'w+') as file:
            file.write(f"{value!r}")
    
        return value
    return wrapper_debug