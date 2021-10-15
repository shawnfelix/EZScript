class Env():
    def __init__(self):
        self.function_defs = []
        #TODO
        
class GlobalEnv(Env):
    def __init__(self):
        self.function_defs = []
        self.klass_defs = []
        self.klasses = []
        self.functions = []
