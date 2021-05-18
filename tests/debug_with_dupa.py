import io
import datetime
from dupa import (
    dupa, wysraj, timeit, debug, print_wrap, fixturize, slow_down)
from dupa.profiling import profile


print("Let's start")
dupa()

@wysraj("pierwsza funkcja")
def fun():
    a = 1
    b = 2
    c = a+b
    dupa("chuj")
    return c

@wysraj("druga funkcja")
def function(a, b):
    dupa("wewnątrz")
    return a + b

@fixturize
def long_running_function(size):
    output = io.StringIO()

    for i in range(size):
        print(f"Position {i}", file=output)
    
    content = output.getvalue()
    output.close()
    return "ok"

@fixturize
def complex_types_passed(stuff):
    return stuff


fun()
result = function(2, 2)
dupa()
print(result)


long_running_function(10000)

complex_types_passed(datetime.datetime.now())


def load_fixtures(function_name):
    
    _calls = f"debug__{function_name}__call.fix"
    _return = f"debug__{function_name}__return.fix"


    with open(_calls) as f:
        call_signature = f.read().strip()


    with open(_return) as f:
        return_signature = f.read().strip()


    assert eval(return_signature) == eval(call_signature), "no chuj się nie udało"


load_fixtures('complex_types_passed')