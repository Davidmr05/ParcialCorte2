# Generated from function.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .functionParser import functionParser
else:
    from functionParser import functionParser

# This class defines a complete listener for a parse tree produced by functionParser.
class functionListener(ParseTreeListener):

    # Enter a parse tree produced by functionParser#prog.
    def enterProg(self, ctx:functionParser.ProgContext):
        pass

    # Exit a parse tree produced by functionParser#prog.
    def exitProg(self, ctx:functionParser.ProgContext):
        pass


    # Enter a parse tree produced by functionParser#stat.
    def enterStat(self, ctx:functionParser.StatContext):
        pass

    # Exit a parse tree produced by functionParser#stat.
    def exitStat(self, ctx:functionParser.StatContext):
        pass


    # Enter a parse tree produced by functionParser#mapFunction.
    def enterMapFunction(self, ctx:functionParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by functionParser#mapFunction.
    def exitMapFunction(self, ctx:functionParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by functionParser#filterFunction.
    def enterFilterFunction(self, ctx:functionParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by functionParser#filterFunction.
    def exitFilterFunction(self, ctx:functionParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by functionParser#expression.
    def enterExpression(self, ctx:functionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by functionParser#expression.
    def exitExpression(self, ctx:functionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by functionParser#opcion.
    def enterOpcion(self, ctx:functionParser.OpcionContext):
        pass

    # Exit a parse tree produced by functionParser#opcion.
    def exitOpcion(self, ctx:functionParser.OpcionContext):
        pass


    # Enter a parse tree produced by functionParser#arith_expression2.
    def enterArith_expression2(self, ctx:functionParser.Arith_expression2Context):
        pass

    # Exit a parse tree produced by functionParser#arith_expression2.
    def exitArith_expression2(self, ctx:functionParser.Arith_expression2Context):
        pass


    # Enter a parse tree produced by functionParser#term2.
    def enterTerm2(self, ctx:functionParser.Term2Context):
        pass

    # Exit a parse tree produced by functionParser#term2.
    def exitTerm2(self, ctx:functionParser.Term2Context):
        pass


    # Enter a parse tree produced by functionParser#factor2.
    def enterFactor2(self, ctx:functionParser.Factor2Context):
        pass

    # Exit a parse tree produced by functionParser#factor2.
    def exitFactor2(self, ctx:functionParser.Factor2Context):
        pass


    # Enter a parse tree produced by functionParser#atom2.
    def enterAtom2(self, ctx:functionParser.Atom2Context):
        pass

    # Exit a parse tree produced by functionParser#atom2.
    def exitAtom2(self, ctx:functionParser.Atom2Context):
        pass


    # Enter a parse tree produced by functionParser#len_expression2.
    def enterLen_expression2(self, ctx:functionParser.Len_expression2Context):
        pass

    # Exit a parse tree produced by functionParser#len_expression2.
    def exitLen_expression2(self, ctx:functionParser.Len_expression2Context):
        pass


    # Enter a parse tree produced by functionParser#index_expression.
    def enterIndex_expression(self, ctx:functionParser.Index_expressionContext):
        pass

    # Exit a parse tree produced by functionParser#index_expression.
    def exitIndex_expression(self, ctx:functionParser.Index_expressionContext):
        pass


    # Enter a parse tree produced by functionParser#capitalize_expression.
    def enterCapitalize_expression(self, ctx:functionParser.Capitalize_expressionContext):
        pass

    # Exit a parse tree produced by functionParser#capitalize_expression.
    def exitCapitalize_expression(self, ctx:functionParser.Capitalize_expressionContext):
        pass


    # Enter a parse tree produced by functionParser#arith_expression_comp.
    def enterArith_expression_comp(self, ctx:functionParser.Arith_expression_compContext):
        pass

    # Exit a parse tree produced by functionParser#arith_expression_comp.
    def exitArith_expression_comp(self, ctx:functionParser.Arith_expression_compContext):
        pass


    # Enter a parse tree produced by functionParser#len_expression.
    def enterLen_expression(self, ctx:functionParser.Len_expressionContext):
        pass

    # Exit a parse tree produced by functionParser#len_expression.
    def exitLen_expression(self, ctx:functionParser.Len_expressionContext):
        pass


    # Enter a parse tree produced by functionParser#id_expression.
    def enterId_expression(self, ctx:functionParser.Id_expressionContext):
        pass

    # Exit a parse tree produced by functionParser#id_expression.
    def exitId_expression(self, ctx:functionParser.Id_expressionContext):
        pass


    # Enter a parse tree produced by functionParser#arith_expression.
    def enterArith_expression(self, ctx:functionParser.Arith_expressionContext):
        pass

    # Exit a parse tree produced by functionParser#arith_expression.
    def exitArith_expression(self, ctx:functionParser.Arith_expressionContext):
        pass


    # Enter a parse tree produced by functionParser#term.
    def enterTerm(self, ctx:functionParser.TermContext):
        pass

    # Exit a parse tree produced by functionParser#term.
    def exitTerm(self, ctx:functionParser.TermContext):
        pass


    # Enter a parse tree produced by functionParser#factor.
    def enterFactor(self, ctx:functionParser.FactorContext):
        pass

    # Exit a parse tree produced by functionParser#factor.
    def exitFactor(self, ctx:functionParser.FactorContext):
        pass


    # Enter a parse tree produced by functionParser#atom.
    def enterAtom(self, ctx:functionParser.AtomContext):
        pass

    # Exit a parse tree produced by functionParser#atom.
    def exitAtom(self, ctx:functionParser.AtomContext):
        pass


    # Enter a parse tree produced by functionParser#comp_operator.
    def enterComp_operator(self, ctx:functionParser.Comp_operatorContext):
        pass

    # Exit a parse tree produced by functionParser#comp_operator.
    def exitComp_operator(self, ctx:functionParser.Comp_operatorContext):
        pass


    # Enter a parse tree produced by functionParser#iterable.
    def enterIterable(self, ctx:functionParser.IterableContext):
        pass

    # Exit a parse tree produced by functionParser#iterable.
    def exitIterable(self, ctx:functionParser.IterableContext):
        pass


    # Enter a parse tree produced by functionParser#list.
    def enterList(self, ctx:functionParser.ListContext):
        pass

    # Exit a parse tree produced by functionParser#list.
    def exitList(self, ctx:functionParser.ListContext):
        pass


    # Enter a parse tree produced by functionParser#tuple.
    def enterTuple(self, ctx:functionParser.TupleContext):
        pass

    # Exit a parse tree produced by functionParser#tuple.
    def exitTuple(self, ctx:functionParser.TupleContext):
        pass


    # Enter a parse tree produced by functionParser#elements.
    def enterElements(self, ctx:functionParser.ElementsContext):
        pass

    # Exit a parse tree produced by functionParser#elements.
    def exitElements(self, ctx:functionParser.ElementsContext):
        pass


    # Enter a parse tree produced by functionParser#expr.
    def enterExpr(self, ctx:functionParser.ExprContext):
        pass

    # Exit a parse tree produced by functionParser#expr.
    def exitExpr(self, ctx:functionParser.ExprContext):
        pass



del functionParser