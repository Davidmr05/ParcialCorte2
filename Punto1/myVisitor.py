from OpComplejasVisitor import OpComplejasVisitor
from OpComplejasParser import OpComplejasParser

class myVisitor(OpComplejasVisitor):
    def __init__(self):
        self.result = None

    def visitOperation(self, ctx):
        left = self.visit(ctx.complexNumber(0))
        right = self.visit(ctx.complexNumber(1))
        op = ctx.op.text  # Usamos el texto del operador directamente
        
        if op == '+':
            self.result = (left[0] + right[0], left[1] + right[1])
        elif op == '-':
            self.result = (left[0] - right[0], left[1] - right[1])
        elif op == '*':
            self.result = ((left[0] * right[0]) - (left[1] * right[1]), (left[0] * right[1]) + (left[1] * right[0]))
        elif op == '/':
            denominator = right[0]**2 + right[1]**2
            self.result = ((left[0] * right[0] + left[1] * right[1]) / denominator, 
                           (left[1] * right[0] - left[0] * right[1]) / denominator)

        # Preparar el resultado para mostrarlo
        sig = " + " if self.result[1] >= 0 else " "
        result = f"{round(self.result[0], 2)}{sig}{round(self.result[1], 2)}j"
        print("El resultado de la operación es:", result)
        return self.result

    def visitComplexNumber(self, ctx):
        real = float(ctx.realPart().getText())
        imaginary = float(ctx.imaginaryPart().getText())
        sign = 1 if ctx.op.text == '+' else -1
        return (real, sign * imaginary)
