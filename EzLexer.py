from sly import Lexer

class EzLexer(Lexer):
    
    tokens = {
    'NAME', 'INTEGER','FLOAT', 'BOOLEAN', 'STRING',
    'PLUS', 'MINUS', 'MULT', 'DIVIDE', 'MODULUS', 
    'COMMA', 
    'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'LCBRACK', 'RCBRACK',
    'AND', 'OR', 'NOT', 'EQ', 'NOTEQ', 'GTE', 'LTE', 'GT', 'LT', 
    'ASSIGN', 'SEMICOLON', 'IF', 'ELSE', 'WHILE', 'PRINT', 'FUNCTION', 'RETURN'}

    literals = {',', '<', '>', '+', '-', '*', '/'}
    
    @_(r'(True|False)')
    def BOOLEAN(self, t):
        t.value = eval(t.value)
        return t

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    NAME['if'] = IF
    NAME['else'] = ELSE
    NAME['while'] = WHILE
    NAME['print'] = PRINT
    NAME['and'] = AND
    NAME['or'] = OR
    NAME['mod'] = MODULUS
    NAME['def'] = FUNCTION
    NAME['return'] = RETURN
    #NAME['class'] = CLASS
    
    @_(r'(\-{0,1}[0-9]*\.[0-9]+|\-{0,1}[0-9]+\.)([Ee][+-]?[0-9]+)?')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t
    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t
    ignore = ' \t'

    @_(r'(\"[^"]*\")|(\'[^\']*\')')
    def STRING(self, t):
        #remove the quotes from string
        t.value = t.value[1 : -1] 
        return t
    
    # DONT MATCH SPACES AND TABS BEFORE THE NUMBER CHECK
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
    

    ASSIGN = r'='
    
    PLUS = r'\+'
    MINUS = r'-'
    MULT = r'\*'
    DIVIDE = r'/'

    # BOOLEAN OPS
    EQ = r'=='
    NOTEQ = r'!='
    NOT = r'!'
    GTE = r'>='
    LTE = r'<='
    GT = r'>'
    LT = r'<'

    COMMA = r','
    SEMICOLON = r';'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACK = r'\['
    RBRACK = r'\]'
    LCBRACK = r'{'
    RCBRACK = r'}'
    
    def error(self, t):
        #self.index += len(self.text)
        raise Exception('SYNTAX ERROR')
