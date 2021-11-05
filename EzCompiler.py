import sys
import os
from EzLexer import EzLexer
from EzParser import * 
from lang.Env import *

def interpreter(name, lexer: EzLexer, parsr: EzParser, debug: bool):
    try:
        # debug
        if debug:
            print("[debug] running - " + name)

            file = open(os.path.join(sys.path[0]+'\\testcases\\', name), 'r')
        else:
            file = open(name, 'r')
        program = file.read()

        tokenized = lexer.tokenize(program)
        #if debug:
        #    for token in tokenized:
        #        print(token)
        ast = parsr.parse(tokenized)
        if ast != None:
            nofuncs = 0
            if len(ast) > 1:
                nofuncs = 1
                for functionDefs in ast[0]:
                    functionDefs.run()
            for node in ast[nofuncs].stmts:
                node.run()
    except Exception as e:
        e = sys.exc_info()[1]
        if False:
            print(e)
        else:
            if (e.args[0] == 'SYNTAX ERROR'):
                print('SYNTAX ERROR')
            else:
                print('SEMANTIC ERROR')

        if debug:
            pass
        else:
            sys.exit()

    # debug        
    if debug:
        print("\n")

def testCompiler(lexer: EzLexer, parsr: EzParser, debug: bool):
    file = open("testcases\\base.ezs", "r")
    program = file.read()

    tokenized = lexer.tokenize(program)
    ast = parsr.parse(tokenized)
    gbl_scope = Scope()
    for klass in ast.klass_defs:
        klass.run()
    for functiondef in ast.function_defs:
        functiondef.run(gbl_scope)
    for stmt in ast.main_def:
        stmt.run()

if __name__ == '__main__':
    debug = False

    lexer = EzLexer()
    parser = EzParser()

    testCompiler(lexer, parser, False)

    #if debug == True:
    #    files = os.listdir(sys.path[0]+'\\testcases\\')
    #    for name in files:
    #        interpreter(name, lexer, parsr, debug)
    #else:
    #    name = str(sys.argv[1])
    #    interpreter(name, lexer, parsr, debug)        
