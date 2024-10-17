# Generated from function.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .functionParser import functionParser
else:
    from functionParser import functionParser

# This class defines a complete generic visitor for a parse tree produced by functionParser.

class functionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by functionParser#prog.
    def visitProg(self, ctx:functionParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#stat.
    def visitStat(self, ctx:functionParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#mapFunction.
    def visitMapFunction(self, ctx:functionParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#filterFunction.
    def visitFilterFunction(self, ctx:functionParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#expression.
    def visitExpression(self, ctx:functionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#opcion.
    def visitOpcion(self, ctx:functionParser.OpcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#arith_expression2.
    def visitArith_expression2(self, ctx:functionParser.Arith_expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#term2.
    def visitTerm2(self, ctx:functionParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#factor2.
    def visitFactor2(self, ctx:functionParser.Factor2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#atom2.
    def visitAtom2(self, ctx:functionParser.Atom2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#len_expression2.
    def visitLen_expression2(self, ctx:functionParser.Len_expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#index_expression.
    def visitIndex_expression(self, ctx:functionParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#capitalize_expression.
    def visitCapitalize_expression(self, ctx:functionParser.Capitalize_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#arith_expression_comp.
    def visitArith_expression_comp(self, ctx:functionParser.Arith_expression_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#len_expression.
    def visitLen_expression(self, ctx:functionParser.Len_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#id_expression.
    def visitId_expression(self, ctx:functionParser.Id_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#arith_expression.
    def visitArith_expression(self, ctx:functionParser.Arith_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#term.
    def visitTerm(self, ctx:functionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#factor.
    def visitFactor(self, ctx:functionParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#atom.
    def visitAtom(self, ctx:functionParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#comp_operator.
    def visitComp_operator(self, ctx:functionParser.Comp_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#iterable.
    def visitIterable(self, ctx:functionParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#list.
    def visitList(self, ctx:functionParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#tuple.
    def visitTuple(self, ctx:functionParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#elements.
    def visitElements(self, ctx:functionParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by functionParser#expr.
    def visitExpr(self, ctx:functionParser.ExprContext):
        return self.visitChildren(ctx)



del functionParser