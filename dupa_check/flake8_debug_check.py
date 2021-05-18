import ast
import sys
from typing import Generator, Tuple, Any, Type, List


WORDS = ['dupa', 'wysraj', 'timeit', 'debug', 'fixturize', 'print_wrap', 'slow_down']

LineNumber = int
Column = int
Word = str

class Visitor(ast.NodeVisitor):

    def __init__(self) -> None:
        self.problems: List[Tuple[LineNumber, Column, Word]] = []

    def _check(self, value: Word) -> bool:
        for word in WORDS:
            if value == word:
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
            yield line, col, f'DUPA002 debug function "{word}" present', type(self)
