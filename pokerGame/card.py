import random

class Card(object):
    #constructor
    def __init__(self,suite,face):
        self._suite = suite
        self._face = face
        self._showCase = ''
        #self._faceShowing = ''
    
    #getter and setter
    @property
    def suite(self):
        return self._suite
    @property
    def face(self):
        return self._face
    
    @suite.setter
    def suite(self, suite):
        self._suite = suite
    @face.setter
    def face(self, face):
        self._face = face


    def makeShowCase(self):
        if(self.face == 1):
            self._showCase = 'A'
        elif(self.face == 11):
            self._showCase = 'J'
        elif(self.face == 12):
            self._showCase = 'Q'
        elif(self.face == 13):
            self._showCase = 'K'
        else:
            self._showCase = self.face
            
    def showCard(self):
        return print(self._suite+str(self._showCase))

    '''overloading operator: < '''
    def __lt__(self, other):
        if(self._face < other._face):
            return True
        else:
            return False

    #TODO: All class function go here

 

