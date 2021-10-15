class KlassDef():
    def __init__(self, name, block):
        self.name = name
        self.block = block
    def run(self):
        nametypes = [str]

        if type(self.name) not in nametypes:
            raise Exception('SEMANTIC ERROR')
        return

class FunctionDef():
    def __init__(self, name, args, block, ret):
        self.name = name
        self.args = args
        self.block = block
        self.ret = ret
    def run(self, global_env):
        nametypes = [str]

        if type(self.name) not in nametypes:
            raise Exception('SEMANTIC ERROR')
        
        #TODO type checking field in self

        # register function in global function 
        global_env.setFunction(self.name, self)