from .Env import Scope
from .Definitions import FunctionDef

class KlassDef():
    def __init__(self, name, params, block):
        self.name = name
        self.block = block
        self.params = params
    def run(self, gbl_scope: Scope):
        # register class in global scope
        gbl_scope.registerKlass(self.name, self)
        return

class KlassField():
    def __init__(self, name, value):
        self.name = name
        self.value = value
class KlassFunction(FunctionDef):
    def __init__(self, name, args, block, ret):
        super(KlassFunction, self).__init__(name, args, block, ret)
class KlassBlock():
    def __init__(self, fields=[], functions=[]):
        self.fields = fields
        self.functions = functions
