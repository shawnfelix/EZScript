class NumericHelper:
    def areBothNumeric(a, b):
        types = [int, float]
        return type(a) in types and type(b) in types
