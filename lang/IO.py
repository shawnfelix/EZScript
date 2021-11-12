class PrintFunction():
    def __init__(self, arg):
        self.arg = arg
    def run(self, scope):
        val = self.arg.run(scope)
        print(val)
