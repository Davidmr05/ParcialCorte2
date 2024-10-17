# Generated from OpComplejas.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,22,8,2,1,2,3,2,25,8,2,1,2,1,2,1,
        3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,1,4,1,0,3,4,29,0,10,1,
        0,0,0,2,13,1,0,0,0,4,17,1,0,0,0,6,28,1,0,0,0,8,30,1,0,0,0,10,11,
        3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,3,4,2,0,14,15,7,0,0,0,15,
        16,3,4,2,0,16,3,1,0,0,0,17,18,5,5,0,0,18,21,3,6,3,0,19,20,7,1,0,
        0,20,22,3,8,4,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,25,
        5,6,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,5,7,0,0,
        27,5,1,0,0,0,28,29,5,8,0,0,29,7,1,0,0,0,30,31,5,8,0,0,31,9,1,0,0,
        0,2,21,24
    ]

class OpComplejasParser ( Parser ):

    grammarFileName = "OpComplejas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "'i'", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_operation = 1
    RULE_complexNumber = 2
    RULE_realPart = 3
    RULE_imaginaryPart = 4

    ruleNames =  [ "program", "operation", "complexNumber", "realPart", 
                   "imaginaryPart" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(OpComplejasParser.OperationContext,0)


        def EOF(self):
            return self.getToken(OpComplejasParser.EOF, 0)

        def getRuleIndex(self):
            return OpComplejasParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = OpComplejasParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.operation()
            self.state = 11
            self.match(OpComplejasParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def complexNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OpComplejasParser.ComplexNumberContext)
            else:
                return self.getTypedRuleContext(OpComplejasParser.ComplexNumberContext,i)


        def getRuleIndex(self):
            return OpComplejasParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = OpComplejasParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.complexNumber()
            self.state = 14
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 15
            self.complexNumber()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def realPart(self):
            return self.getTypedRuleContext(OpComplejasParser.RealPartContext,0)


        def imaginaryPart(self):
            return self.getTypedRuleContext(OpComplejasParser.ImaginaryPartContext,0)


        def getRuleIndex(self):
            return OpComplejasParser.RULE_complexNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexNumber" ):
                listener.enterComplexNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexNumber" ):
                listener.exitComplexNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexNumber" ):
                return visitor.visitComplexNumber(self)
            else:
                return visitor.visitChildren(self)




    def complexNumber(self):

        localctx = OpComplejasParser.ComplexNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_complexNumber)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(OpComplejasParser.T__4)
            self.state = 18
            self.realPart()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==4:
                self.state = 19
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.imaginaryPart()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 23
                self.match(OpComplejasParser.T__5)


            self.state = 26
            self.match(OpComplejasParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(OpComplejasParser.NUMBER, 0)

        def getRuleIndex(self):
            return OpComplejasParser.RULE_realPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealPart" ):
                listener.enterRealPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealPart" ):
                listener.exitRealPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealPart" ):
                return visitor.visitRealPart(self)
            else:
                return visitor.visitChildren(self)




    def realPart(self):

        localctx = OpComplejasParser.RealPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_realPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(OpComplejasParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImaginaryPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(OpComplejasParser.NUMBER, 0)

        def getRuleIndex(self):
            return OpComplejasParser.RULE_imaginaryPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImaginaryPart" ):
                listener.enterImaginaryPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImaginaryPart" ):
                listener.exitImaginaryPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImaginaryPart" ):
                return visitor.visitImaginaryPart(self)
            else:
                return visitor.visitChildren(self)




    def imaginaryPart(self):

        localctx = OpComplejasParser.ImaginaryPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_imaginaryPart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(OpComplejasParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





