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
    def defSymbol(self, name, type, value):
        if (self.table.get(name) != None):
            raise Exception('Symbol already defined for: ' + name)
        
        symb = Symbol(name, type, value)
        self.table[name] = symb
        
    def setSymbol(self, name, type, value):
        if (self.table.get(name) == None):
            raise Exception('No symbol defined for: ' + name)

        newObj = Symbol(name, type, value)
        self.table[name] = newObj

    def getSymbol(self, name):
        if (self.table.get(name) == None):
            raise Exception('No symbol defined for: ' + name)
        val = self.table.get(name)
        return val.value

class Scope():
    function_defs = {}
    klass_defs = {}
    symbol_table = SymbolTable()
    def __init__(self):
        pass
    def run(self):
        return [self.symbol_table, self.function_defs, self.klass_defs]
    def registerKlass(self, name, klass):
        self.klass_defs[name] = klass
    def registerFunction(self, name, function):
        self.function_defs[name] = function
    def getSymbol(self, name):
        return self.symbol_table.getSymbol(name)
    def defSymbol(self, name, type, value):
        self.symbol_table.defSymbol(name, type, value)
    def setSymbol(self, name, type, value):
        self.symbol_table.setSymbol(name, type, value)

class DerefVarOp():
    def __init__(self, name):
        self.name = name
        return
    def run(self, scope:Scope):
        return scope.getSymbol(self.name)