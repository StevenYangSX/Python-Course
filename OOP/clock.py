import time

class Clock(object):
    #__slots__ = ("_h","_m","_s")

    def __init__(self, h, m, s):
        self._h = h
        self._m = m
        self._s = s

    #TODO: getters
    # @property
    # def getH(self):
    #     return self._h
    # @property
    # def getM(self):
    #     return self._m

    # @property
    # def getS(self):
    #     return self._s

    #TODO: setters
    # @h.setter
    # def h(self, h):
    #     self._h = h
    
    # @m.setter
    # def m(self, m):
    #     self._m = m

    # @s.setter
    # def s(self, s):
    #     self._s = s

    #TODO: run   tip : sleep(1)
    #@staticmethod
    def run(self):
        while True:
            if(self._s <= 59):
                self._s += 1






#matin
clock = Clock(0,0,0)
clock.run()