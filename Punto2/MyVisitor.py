#MyVisitor

from functionParser import functionParser
from functionVisitor import functionVisitor

class myVisitor(functionVisitor):
    def __init__(self):
        self.result = None
        
        



    

    def visitFilterFunction(self, ctx):
        function_name = ctx.expression().getText()
        
        function_name = "lambda x: " + function_name
        iterable_elements = ctx.iterable().getText()
        iterable_elements=list(iterable_elements[1:-1].split(','))
        if iterable_elements[0].isdigit():
            iterable_elements=list(map(int,iterable_elements))
        
        result=list(filter(eval(function_name),iterable_elements))
        print(result)
        return result
    
    def visitMapFunction(self, ctx):
        function_name = ctx.opcion().getText()
        function_name = "lambda x: " + function_name
        iterable_elements = ctx.iterable().getText()
        iterable_elements=list(iterable_elements[1:-1].split(','))
        iterable_elements = [elem.strip(' "') if elem.startswith('"') else elem for elem in iterable_elements]

        if iterable_elements[0].isdigit():
            iterable_elements=list(map(int,iterable_elements))
        
        result=list(map(eval(function_name),iterable_elements))
        print(result)
        return result
    
    

    def visitmapFunction(self, ctx):
        print(ctx.mapFunction())
        return ctx.mapFunction().getText()

    def visitElements(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]