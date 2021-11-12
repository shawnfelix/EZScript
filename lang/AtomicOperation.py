from helper import NumericHelper
from errors import SemanticError
from .Env import Scope
class SumOp:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def run(self, scope):
        types = [int, float, str, list]
        l = self.l.run(scope)
        r = self.r.run(scope)
        if ((type(l) in types and type(r) in types) #are in types
            and (NumericHelper.areBothNumeric(l, r) or type(l) == type(r))):
            # int, float  - math addition
            # arrays - array arithmetic or maybe concat
            # string, list - concatenation 
            return l + r
        else:
            raise Exception(SemanticError.error("Addition operation must be between two number types"))
class SubtractionOp: #done
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def run(self, scope):
        l = self.l.run(scope)
        r = self.r.run(scope)
        #ints or reals only
        types = [int, float]
        if type(l) not in types or type(r) not in types:
            raise Exception(SemanticError.error("Subtraction operation must be between two number types"))
        return l - r

class MultiplicationOp:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def run(self, scope):
        l = self.l.run(scope)
        r = self.r.run(scope)
        # ints or reals only
        types = [int, float]
        if type(l) not in types or type(r) not in types:
            raise Exception('SEMANTIC ERROR') #TODO error messages

        return l * r

class DivisionOp():
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def run(self, scope):
        l = self.l.run(scope)
        r = self.r.run(scope)
        try:
            # cant divide by zero
            if r == 0:
                raise Exception('SEMANTIC ERROR') #TODO error messages
            return l / r
        except:
            raise Exception('SEMANTIC ERROR') #TODO error messages

class AssignmentOp():
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    def run(self, scope:Scope):
        val = self.expr.run(scope)
        scope.setSymbol(self.name, None, val)
        return
