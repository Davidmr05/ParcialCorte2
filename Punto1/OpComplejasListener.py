# Generated from OpComplejas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OpComplejasParser import OpComplejasParser
else:
    from OpComplejasParser import OpComplejasParser

# This class defines a complete listener for a parse tree produced by OpComplejasParser.
class OpComplejasListener(ParseTreeListener):

    # Enter a parse tree produced by OpComplejasParser#program.
    def enterProgram(self, ctx:OpComplejasParser.ProgramContext):
        pass

    # Exit a parse tree produced by OpComplejasParser#program.
    def exitProgram(self, ctx:OpComplejasParser.ProgramContext):
        pass


    # Enter a parse tree produced by OpComplejasParser#operation.
    def enterOperation(self, ctx:OpComplejasParser.OperationContext):
        pass

    # Exit a parse tree produced by OpComplejasParser#operation.
    def exitOperation(self, ctx:OpComplejasParser.OperationContext):
        pass


    # Enter a parse tree produced by OpComplejasParser#complexNumber.
    def enterComplexNumber(self, ctx:OpComplejasParser.ComplexNumberContext):
        pass

    # Exit a parse tree produced by OpComplejasParser#complexNumber.
    def exitComplexNumber(self, ctx:OpComplejasParser.ComplexNumberContext):
        pass


    # Enter a parse tree produced by OpComplejasParser#realPart.
    def enterRealPart(self, ctx:OpComplejasParser.RealPartContext):
        pass

    # Exit a parse tree produced by OpComplejasParser#realPart.
    def exitRealPart(self, ctx:OpComplejasParser.RealPartContext):
        pass


    # Enter a parse tree produced by OpComplejasParser#imaginaryPart.
    def enterImaginaryPart(self, ctx:OpComplejasParser.ImaginaryPartContext):
        pass

    # Exit a parse tree produced by OpComplejasParser#imaginaryPart.
    def exitImaginaryPart(self, ctx:OpComplejasParser.ImaginaryPartContext):
        pass



del OpComplejasParser