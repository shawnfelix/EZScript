from .Env import Scope

class KlassDef():
    def __init__(self, name, block):
        self.name = name
        self.block = block
    def run(self, gbl_scope: Scope):
        # create scope for the klass
        scope = Scope()

        # register field and function definitions
        

        nametypes = [str]

        if type(self.name) not in nametypes:
            raise Exception('SEMANTIC ERROR')
        return

class KlassField():
    def __init__(self, name, value):
        self.name = name
        self.value = value