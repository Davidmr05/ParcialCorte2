#main.py

from antlr4 import *
from functionLexer import functionLexer
from functionParser import functionParser
from functionVisitor import functionVisitor
from MyVisitor import myVisitor

def main():
    input_stream = FileStream('input.txt')
    lexer = functionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = functionParser(stream)
    tree = parser.prog()

    visitor = myVisitor()
    visitor.visit(tree)
    
    

if __name__ == '__main__':
    main()