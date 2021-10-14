class Error():
    msg = "ERROR"

class SemanticError(Error):
    ROOT_MSG = "[Semantic Error]: "
    def error(value,self):
        return self.ROOT_MSG + value;