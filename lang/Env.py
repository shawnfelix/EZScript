class Symbol():
    name = ""
    type = None
    value = None
    def __init__(self, name, type, value):
        self.name = name
        self.value = value
        self.type = type
    def set(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    def set(self, value):
        self.value = value
    def get(self):
        return self.value
    def type(self):
        return self.type
class SymbolTable():
    def __init__(self):
        self.table = {}
    def defineObject(self, name, type, value):
        if (self.table.get(name) != None):
            raise Exception('Symbol already defined for: ' + name)
        
        symb = Symbol(name, type)
        
    def setObject(self, name, type, value):
        if (self.table.get(name) == None):
            raise Exception('No symbol defined for: ' + name)

        newObj = Symbol(name, value, type)
        self.table.insert(name, newObj)

    def getObject(self, name):
        if (self.table.get(name) == None):
            raise Exception('No symbol defined for: ' + name)
        return self.table.get(name)

class Scope():
    function_defs = []
    klass_defs = []
    symbol_table = SymbolTable()
    def __init__(self):
        pass
    def run(self):
        return [self.symbol_table, self.function_defs, self.klass_defs]