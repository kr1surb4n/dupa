from typing import Set
import ast
from dupa_check.flake8_debug_check import Plugin, WORDS


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}

def test_if_dupa_in_words():
    assert 'dupa' in WORDS

def test_trivial_case():
    assert _results('') == set()

def test_debug_checker():
    assert _results('wysraj()') == {'1:0 DUPA002 debug function "wysraj" present'}
    assert _results('dupa()') == {'1:0 DUPA002 debug function "dupa" present'}
    assert _results('print_wrap()') == {'1:0 DUPA002 debug function "print_wrap" present'}
    assert _results('timeit()') == {'1:0 DUPA002 debug function "timeit" present'}
    assert _results('debug()') == {'1:0 DUPA002 debug function "debug" present'}
    assert _results('fixturize()') == {'1:0 DUPA002 debug function "fixturize" present'}
    assert _results('slow_down()') == {'1:0 DUPA002 debug function "slow_down" present'}

def test_decorators():
    code = "@wysraj\ndef f():\n\tpass"
    assert _results(code) == {'1:1 DUPA002 debug function "wysraj" present'}

    code = "@dupa\ndef f():\n\tpass"
    assert _results(code) == {'1:1 DUPA002 debug function "dupa" present'}


def test_a_file():
    with open('tests/debug_with_dupa.py') as f:
        content = f.read()

    assert len(_results(content)) == 6