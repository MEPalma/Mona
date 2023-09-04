import abc
import sys
from typing import Tuple

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener

from mona.gen.GramLexer import GramLexer
from mona.gen.GramParser import GramParser
from mona.interpreter.component.program import Program
from mona.interpreter.component_store import ComponentStore
from mona.interpreter.parsing.preprocessor import Preprocessor


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Parsing error at {line}:{column}, {msg}", file=sys.stderr, flush=True)
        sys.exit(2)


class Parser(abc.ABC):
    @staticmethod
    def parse(src: str) -> Tuple[Program, ComponentStore]:
        input_stream = InputStream(src)
        lexer = GramLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GramParser(stream)
        parser.addErrorListener(MyErrorListener())
        tree = parser.program()
        preprocessor = Preprocessor()
        program: Program = preprocessor.visit(tree)
        return program, preprocessor.comp_store
