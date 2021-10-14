from sly import Parser
from EzLexer import EzLexer
from helper import NumericHelper
from errors import SemanticError


class SumOp:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def run(self):
        types = [int, float, str, list]
        l = self.l.run()
        r = self.r.run()
        try:
            if ((type(l) in types and type(r) in types) #are in types
                and (NumericHelper.areBothNumeric(l, r) or type(l) == type(r))):
                # int, float  - math addition
                # arrays - array arithmetic or maybe concat
                # string, list - concatenation 
            
                print(l + r)
                return l + r
            else:
                raise Exception(SemanticError.error("Addition operation must be between two number types"))
        except:
            raise Exception('SEMANTIC ERROR')

class Atomic:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def __neg__(self):
        return Atomic (-self.value, self.type) # negation
    def run(self):
        return self.value

class EzParser(Parser):
    tokens = EzLexer.tokens
    literals = EzLexer.literals

    #precedence = (
    #    ('left', ORELSE),
    #    ('left', ANDALSO),
    #    ('left', NOT),
    #    ('left', EQ, NOTEQ, GT, LT, GTE, LTE),
    #    ('left', PLUS, MINUS),
    #    ('left', MULT, DIVIDE, MODULUS),
    #    ('left', LBRACK, RBRACK),
    #    ('left', LPAREN, RPAREN),
    #    ('right', NEGATION),
    #    ('left', PARENEXPR),
    #    ('left', FLOAT, INTEGER, BOOLEAN),
    #    ('right', ASSIGN),
    #)
    #precedence = (
    #    ('left', PLUS, MINUS),
    #)

    @_('statements')
    def file(self, p):
        return p.statements
    
    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements
    @_('')
    def statements(self, p):
        return []

    @_('s_stmt')
    def statement(self, p):
        return p.s_stmt

    # ATOMICS
    @_('INTEGER')
    def atom(self, p):
        return Atomic(p.INTEGER, int)
    @_('STRING')
    def atom(self, p):
        return Atomic(p.STRING, str)
    @_('FLOAT')
    def atom(self, p):
        return Atomic(p.FLOAT, float)
    @_('BOOLEAN')
    def atom(self, p):
        return Atomic(p.BOOLEAN, bool)
    
    @_('')
    # OPERATIONS
    @_('atom PLUS atom SEMICOLON')
    def s_stmt(self, p):
        return SumOp(p.atom0, p.atom1)
    