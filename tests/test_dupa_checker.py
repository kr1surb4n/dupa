from typing import Set
import ast
from dupa_check.flake8_dupa_check import Plugin, WORDS


def _results(s: str) -> Set[str]:
    tree = ast.parse(s)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}

def test_if_dupa_in_words():
    assert 'dupa' in WORDS

def test_trivial_case():
    assert _results('') == set()

def test_dupa_checker():
    assert _results('"dupa"') == {'1:0 DUPA001 word "dupa" present'}
    assert _results('dupa()') == {'1:0 DUPA001 word "dupa" present'}

    code = "@dupa\ndef f():\n\tpass"
    assert _results(code) == {'1:1 DUPA001 word "dupa" present'}

    assert _results('"wysraj"') == {'1:0 DUPA001 word "wysraj" present'}
    assert _results('wysraj()') == {'1:0 DUPA001 word "wysraj" present'}

    code = "@wysraj\ndef f():\n\tpass"
    assert _results(code) == {'1:1 DUPA001 word "wysraj" present'}

    assert _results('"ass"') == {'1:0 DUPA001 word "ass" present'}
    assert _results('"dildo"') == {'1:0 DUPA001 word "dildo" present'}

def test_startwith_curseword():
    assert _results('"dupek"') == {'1:0 DUPA001 word "dupek" present'}
    assert _results('chujowy()') == {'1:0 DUPA001 word "chujowy" present'}

def test_a_file():
    with open('tests/debug_with_dupa.py') as f:
        content = f.read()

    assert len(_results(content)) == 7