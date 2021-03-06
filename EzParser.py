from sly import Parser
from EzLexer import EzLexer
from helper import NumericHelper
import lang
from lang.Definitions import MainDef 

class Atomic:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def __neg__(self, scope):
        return Atomic (-self.value, self.type) # negation
    def run(self, scope):
        return self.value

class FileDefs():
    def __init__(self):
        self.function_defs = []
        self.klass_defs = []
        self.main_def = None

class EzParser(Parser):
    debugfile = 'debug.out'
    tokens = EzLexer.tokens
    literals = EzLexer.literals

    parse_bucket = FileDefs()
    precedence = (
        ('left', ELSE),
        ('left', AND),
        ('left', NOT),
        ('left', EQ, NOTEQ, GT, LT, GTE, LTE),
        ('left', PLUS, MINUS),
        ('left', MULT, DIVIDE, MODULUS),
        ('left', LBRACK, RBRACK),
        ('left', LPAREN, RPAREN),
        #('right', NEGATION),
        #('left', PARENEXPR),
        ('left', FLOAT, INTEGER, BOOLEAN),
        ('right', ASSIGN),
    )
    #precedence = (
    #    ('left', PLUS, MINUS),
    #)

    @_('statements')
    def file(self, p):
        return self.parse_bucket
    @_('')
    def empty(self, p):
        pass

    @_('statement statements')
    def statements(self, p):
        if isinstance(p.statement, lang.FunctionDef):
            self.parse_bucket.function_defs.append(p.statement)
        elif isinstance(p.statement, lang.KlassDef):
            self.parse_bucket.klass_defs.append(p.statement)
        elif isinstance(p.statement, lang.MainDef):
            self.parse_bucket.main_def = p.statement

        return self.parse_bucket
    @_('empty')
    def statements(self, p):
        return []

    # BLOCK (SMALL STATEMENTS BLOCK)
    @_('LCBRACK s_stmts RCBRACK')
    def block(self, p):
        return p.s_stmts

    # CLASS BLOCK 
    @_('LCBRACK klass_stmts RCBRACK')
    def klassblock(self, p):
        # create class block and append all definitions to it
        kblock = lang.KlassBlock()
        for stmt in p.klass_stmts:
            if isinstance(stmt, lang.FunctionDef):
                kblock.functions = kblock.functions + [lang.KlassFunction(stmt.name, stmt.args, stmt.block, stmt.ret)]
            elif isinstance(stmt, lang.KlassField):
                kblock.functions = kblock.functions + [stmt]
        return kblock

    @_('klass_field',
        'function_def',
        'klass_def')
    def klass_stmt(self, p):
        return p[0]

    @_('NAME SEMICOLON')
    def klass_field(self, p):
        return lang.KlassField(p.NAME, None)

    @_('NAME ASSIGN expr SEMICOLON')
    def klass_field(self, p):
        return lang.KlassField(p.NAME, p.expr)

    @_('klass_stmt klass_stmts')
    def klass_stmts(self, p):
        return [p.klass_stmt] + p.klass_stmts
    @_('empty')
    def klass_stmts(self, p):
        return []

    @_('s_stmt SEMICOLON s_stmts')
    def s_stmts(self, p):
        return [p.s_stmt] + p.s_stmts
    @_('empty')
    def s_stmts(self, p):
        return []
    
    @_('s_stmt SEMICOLON')
    def statement(self, p):
        return p.s_stmt
    @_('c_stmt')
    def statement(self, p):
        return p.c_stmt
    #TODO e_stmt def


    @_('klass_def',
       'function_def',
       'main_def')
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
    @_('NAME')
    def atom(self, p):
        return lang.DerefVarOp(p.NAME)

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

    # MAIN DEFINITION
    @_('MAIN LPAREN RPAREN block')
    def main_def(self, p):
        return lang.MainDef(p.block)

    # CLASS DEFINITIONS
    @_('KLASS NAME LPAREN params RPAREN klassblock')
    def klass_def(self, p):
        return lang.KlassDef(p.NAME, p.params, p.klassblock)
    
    # FUNCTION DEFINITIONS
    @_('FUNCTION NAME LPAREN params RPAREN block')
    def function_def(self, p):
        return lang.FunctionDef(p.NAME, p.params, p.block, None)

    # VARIABLE DEFINITIONS
    @_('VAR NAME')
    def variabledef(self, p):
        return lang.VariableDef(p.NAME, None, None)
    
    # ASSIGNMENT
    @_('assignment',
        'variabledef')
    def s_stmt(self, p):
        return p[0]
    @_('VAR NAME ASSIGN expr')
    def variabledef(self, p):
        return lang.VariableDef(p.NAME, p.expr, None)
    @_('NAME ASSIGN expr')
    def assignment(self, p):
        return lang.AssignmentOp(p.NAME, p.expr)

    
    # OPERATIONS
    @_('atom PLUS atom')
    def expr(self, p):
        return lang.SumOp(p.atom0, p.atom1)
    @_('atom MINUS atom')
    def expr(self, p):
        return lang.SubtractionOp(p.atom0, p.atom1)
    @_('atom MULT atom')
    def expr(self, p):
        return lang.MultiplicationOp(p.atom0, p.atom1)
    @_('atom DIVIDE atom')
    def expr(self, p):
        return lang.DivisionOp(p.atom0, p.atom1)

    @_('atom')
    def expr(self, p):
        return p.atom

    # BUILT IN FUNCTIONS
    @_('PRINT LPAREN expr RPAREN')
    def s_stmt(self, p):
        return lang.PrintFunction(p.expr)