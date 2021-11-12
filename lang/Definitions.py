from .Env import Scope

class MainDef():
    def __init__(self, block):
        self.block = block
    def run(self, env):
        for stmt in self.block:
            stmt.run(env)
        return 

# Functions can be defined in either a class scope or file scope
class FunctionDef():
    def __init__(self, name, args, block, ret):
        self.name = name
        self.args = args
        self.block = block
        self.ret = ret
    def run(self, scope: Scope):
        # register the fuction in parent scope
        scope.registerFunction(self.name, self)
        return

class VariableDef():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type
    def run(self, global_env):
        pass #TODO