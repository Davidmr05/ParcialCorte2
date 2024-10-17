#main.py

from antlr4 import *
from fourierLexer import fourierLexer
from fourierParser import fourierParser
from fourierVisitor import fourierVisitor
from MyVisitor import myVisitor

def main():
    
    input_stream = FileStream('input.txt')
    lexer = fourierLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fourierParser(stream)
    tree = parser.prog()

    visitor = myVisitor()
    visitor.visit(tree)
    
    

if __name__ == '__main__':
    main()