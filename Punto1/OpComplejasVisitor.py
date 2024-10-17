# Generated from OpComplejas.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OpComplejasParser import OpComplejasParser
else:
    from OpComplejasParser import OpComplejasParser

# This class defines a complete generic visitor for a parse tree produced by OpComplejasParser.

class OpComplejasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OpComplejasParser#program.
    def visitProgram(self, ctx:OpComplejasParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpComplejasParser#operation.
    def visitOperation(self, ctx:OpComplejasParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpComplejasParser#complexNumber.
    def visitComplexNumber(self, ctx:OpComplejasParser.ComplexNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpComplejasParser#realPart.
    def visitRealPart(self, ctx:OpComplejasParser.RealPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OpComplejasParser#imaginaryPart.
    def visitImaginaryPart(self, ctx:OpComplejasParser.ImaginaryPartContext):
        return self.visitChildren(ctx)



del OpComplejasParser