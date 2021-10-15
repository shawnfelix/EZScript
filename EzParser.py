from sly import Parser
from EzLexer import EzLexer
from helper import NumericHelper
import astnodes 

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
    @_('')
    def empty(self, p):
        pass

    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements
    @_('empty')
    def statements(self, p):
        return []

    @_('LCBRACK s_stmts RCBRACK')
    def block(self, p):
        return p.s_stmts
    

    @_('s_stmt SEMICOLON s_stmts')
    def s_stmts(self, p):
        return [p.s_stmt] + p.s_stmts
    @_('empty')
    def s_stmts(self, p):
        return []
    
    @_('s_stmt')
    def statement(self, p):
        return p.s_stmt
    @_('c_stmt')
    def statement(self, p):
        return p.c_stmt
    #TODO e_stmt def


    @_('klass_def',
       'function_def')
    def c_stmt(self, p):
        return p[0]

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
    
    
    # OPERATIONS
    @_('atom PLUS atom')
    def s_stmt(self, p):
        return astnodes.SumOp(p.atom0, p.atom1)
    @_('atom MINUS atom')
    def s_stmt(self, p):
        return astnodes.SubtractionOp(p.atom0, p.atom1)
    @_('atom MULT atom')
    def s_stmt(self, p):
        return astnodes.MultiplicationOp(p.atom0, p.atom1)
    @_('atom DIVIDE atom')
    def s_stmt(self, p):
        return astnodes.DivisionOp(p.atom0, p.atom1)

    # PARAMETERS
    @_('NAME')
    def param(self, p):
        return p.NAME #TODO define param variable in relevant scope?
    @_('param COMMA params')
    def params(self, p):
        return [p.param] + p.params
    @_('empty')
    def params(self, p):
        return []

    # CLASS DEFINITIONS
    @_('KLASS NAME LPAREN RPAREN block')
    def klass_def(self, p):
        return astnodes.KlassDef(p.NAME, p.block)
    @_('KLASS NAME LPAREN params RPAREN block')
    def klass_def(self, p):
        return astnodes.KlassDef(p.NAME, p.params, p.block)
    
    # FUNCTION DEFINITIONS
    @_('FUNCTION NAME LPAREN RPAREN block')
    def function_def(self, p):
        return astnodes.FunctionDef(p.NAME, p.block)
    @_('FUNCTION NAME LPAREN params RPAREN block')
    def function_def(self, p):
        return astnodes.FunctionDef(p.NAME, p.block)
    