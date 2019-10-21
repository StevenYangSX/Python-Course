class Triangel(object):

    __slot__ = ("_a","_b","_c")

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod # can be called without instantiating a object
    def isValid(a,b,c):
        return a+b > c and a+c > b and b+c > a


