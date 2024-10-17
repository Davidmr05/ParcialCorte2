# Generated from fourier.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fourierParser import fourierParser
else:
    from fourierParser import fourierParser

# This class defines a complete generic visitor for a parse tree produced by fourierParser.

class fourierVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fourierParser#prog.
    def visitProg(self, ctx:fourierParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#start.
    def visitStart(self, ctx:fourierParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Recta.
    def visitRecta(self, ctx:fourierParser.RectaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Triang.
    def visitTriang(self, ctx:fourierParser.TriangContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Sign.
    def visitSign(self, ctx:fourierParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#U.
    def visitU(self, ctx:fourierParser.UContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#D.
    def visitD(self, ctx:fourierParser.DContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Cos.
    def visitCos(self, ctx:fourierParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Sin.
    def visitSin(self, ctx:fourierParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#Sum.
    def visitSum(self, ctx:fourierParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#parameters.
    def visitParameters(self, ctx:fourierParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#parameters1.
    def visitParameters1(self, ctx:fourierParser.Parameters1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#parameters2.
    def visitParameters2(self, ctx:fourierParser.Parameters2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#parameters3.
    def visitParameters3(self, ctx:fourierParser.Parameters3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#inr.
    def visitInr(self, ctx:fourierParser.InrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#inr2.
    def visitInr2(self, ctx:fourierParser.Inr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#inr3.
    def visitInr3(self, ctx:fourierParser.Inr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#inr4.
    def visitInr4(self, ctx:fourierParser.Inr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#inr5.
    def visitInr5(self, ctx:fourierParser.Inr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fourierParser#comp_operator.
    def visitComp_operator(self, ctx:fourierParser.Comp_operatorContext):
        return self.visitChildren(ctx)



del fourierParser