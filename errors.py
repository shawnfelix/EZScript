class Error():
    msg = "ERROR"

class SemanticError(Error):
    ROOT_MSG = "[Semantic Error]: "

    @staticmethod
    def error(value):
        return SemanticError.ROOT_MSG + value