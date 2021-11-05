class PrintFunction():
    def __init__(self, arg):
        self.arg = arg
    def run(self, env):
        val = self.arg.run(env)
        print(val)
