import sys
from antlr4 import *
from OpComplejasLexer import OpComplejasLexer
from OpComplejasParser import OpComplejasParser
from myVisitor import myVisitor

def main(argv):
    # Abrir y leer el archivo de entrada
    with open("input.txt", "r") as file:
        for line in file:
            input_stream = InputStream(line.strip())
            lexer = OpComplejasLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = OpComplejasParser(stream)
            tree = parser.program()

            # Usar el visitante para procesar la operación
            visitor = myVisitor()
            visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
