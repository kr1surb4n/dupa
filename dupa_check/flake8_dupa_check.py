import ast
import os
import glob
from typing import Generator, Tuple, Any, Type, List

WORDS = []

def init_words():
    global WORDS
    this_dir = os.path.abspath(os.path.dirname(__file__))
    search_path = os.path.join(this_dir, 'words/*')

    for f in glob.glob(search_path, recursive=True):
        with open(f) as file:
            WORDS += list(file)
    WORDS = list(map(str.strip, WORDS))
init_words()


LineNumber = int
Column = int
Word = str


class Visitor(ast.NodeVisitor):

    def __init__(self) -> None:
        self.problems: List[Tuple[LineNumber, Column, Word]] = []

    def _check(self, value: Word) -> bool:
        global WORDS
        for word in WORDS:
            if value == word or str(value).startswith(word):
                return True

    def visit_Constant(self, node: ast.Constant) -> None:
        if self._check(node.value):
            self.problems += [(node.lineno, node.col_offset, node.value)]
            
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        if self._check(node.id):
            self.problems += [(node.lineno, node.col_offset, node.id)]
            
        self.generic_visit(node)



class Plugin:
    name = __name__
    version = '0.0.1'

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col, word in visitor.problems:
            yield line, col, f'DUPA001 word "{word}" present', type(self)
