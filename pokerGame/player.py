from poker import Poker
from card import Card

class Player(object):
    #constructor
    def __init__(self,name):
        self._name = name
        self._cardsInHand = []
        self._cardsType = ""
    #getter and setter
    @property
    def name(self):
        return self._name
    @property
    def cardsInHand(self):
        return self._cardsInHand
    

    def getCard(self, card):
        """摸牌"""
        self._cardsInHand.append(card)
    
    #TODO: arrange cards in hand to make comparison easier
    def arrange(self):
        """玩家整理手上的牌"""
        self._cardsInHand.sort(reverse = True)

    #find the type of cards in hand
    # def ifFlush(self):
    #     if((self.cardsInHand[0].suite == self.cardsInHand[1].suite) and 
    #         (self.cardsInHand[1].suite == self.cardsInHand[2].suite) and 
    #         (self.cardsInHand[2].suite == self.cardsInHand[3].suite) and
    #         (self.cardsInHand[3].suite == self.cardsInHand[4].suite) ):
    #         self._cardsType = 'Flush'
    def findType(self):
        if(all(self._cardsInHand[i] == self._cardsInHand[i+1] for i in range(0,3)) or
            all(self._cardsInHand[i] == self._cardsInHand[i+1] for i in range(1,4))):
            self._cardsType = 'Four Of A Kind'
        elif((self._cardsInHand[0].suite == self._cardsInHand[1].suite) and 
            (self._cardsInHand[1].suite == self._cardsInHand[2].suite) and 
            (self._cardsInHand[2].suite == self._cardsInHand[3].suite) and
            (self._cardsInHand[3].suite == self._cardsInHand[4].suite) ):
            self._cardsType = 'Flush'
        #print(self._cardsType)
        elif(((self._cardsInHand[0].face == self._cardsInHand[1].face) and 
             (self._cardsInHand[1].face == self._cardsInHand[2].face) and 
             (self._cardsInHand[3].face == self._cardsInHand[4].face)) or (
                 (self._cardsInHand[0].face == self._cardsInHand[1].face) and 
                 (self._cardsInHand[2].face == self._cardsInHand[3].face) and
                 (self._cardsInHand[3].face == self._cardsInHand[4].face)
             )):
             self._cardsType ='Full House'
        elif(all((self._cardsInHand[i].face - self._cardsInHand[i + 1].face) == 1 for i in range(0,4))):
            self._cardsType = 'Straight' 

        elif(((self._cardsInHand[0].face == self._cardsInHand[1].face) and 
             (self._cardsInHand[1].face == self._cardsInHand[2].face) or
             ((self._cardsInHand[1].face == self._cardsInHand[2].face) and 
             (self._cardsInHand[2].face == self._cardsInHand[3].face)) or 
             ((self._cardsInHand[2].face == self._cardsInHand[3].face) and 
             (self._cardsInHand[3].face == self._cardsInHand[4].face)))):
             self._cardsType = 'Three Of A Kind'
        elif(((self._cardsInHand[0].face == self._cardsInHand[1].face) and 
              (self._cardsInHand[2].face == self._cardsInHand[3].face)) or
              ((self._cardsInHand[1].face == self._cardsInHand[2].face) and 
              (self._cardsInHand[3].face == self._cardsInHand[4].face)) or
              ((self._cardsInHand[0].face == self._cardsInHand[1].face) and 
              (self._cardsInHand[3].face == self._cardsInHand[4].face))):
              self._cardsType = 'Two Pairs'
        elif((self._cardsInHand[0].face == self._cardsInHand[1].face) or
             (self._cardsInHand[1].face == self._cardsInHand[2].face) or
             (self._cardsInHand[2].face == self._cardsInHand[3].face) or
             (self._cardsInHand[3].face == self._cardsInHand[4].face)):
             self._cardsType = 'One Pair'
        else:
            self._cardsType = 'High Card'  
          
        #print("Type is :",self._cardsType)
    
    def ifFlushStraight(self):
        if(self._cardsType == 'Flush' and 
            all((self._cardsInHand[i].face - self._cardsInHand[i + 1].face) == 1 for i in range(0,4))):
            self._cardsType = 'Flush Straight'


        



    #TODO: show cards in hand
    def showCardsInHand(self):
        for item in self._cardsInHand:
            item.showCard()


    '''overloading < operators'''
    def __lt__(self, other):
        if(self._cardsType != other._cardsType ):
            if(self._cardsType == 'Flush Straight'):
                return False
            elif(self._cardsType == 'Four Of A Kind' and other._cardsType != 'Flush Straight'):
                return False
            elif(self._cardsType == 'Full House' and other._cardsType != 'Flush' 
                    and other._cardsType != 'Four Of A Kink'):
                    return False
            elif(self._cardsType == 'Flush' and other._cardsType != 'Flush Straight' and 
                    other._cardsType != 'Four Of A Kind' and other._cardsType != 'Full House'):
                    return False
            elif(self._cardsType == 'Straight' and other._cardsType != 'Flush Straight' and 
                    other._cardsType != 'Four Of A Kind' and other._cardsType != 'Full House' and 
                    other._cardsType != 'Flush' ):
                    return False
            elif(self._cardsType == 'Three Of A Kind' and other._cardsType != 'Flush Straight' and 
                    other._cardsType != 'Four Of A Kind' and other._cardsType != 'Full House' and 
                    other._cardsType != 'Flush' and other._cardsType != 'Straight'):
                    return False
            elif(self._cardsType == 'Two Pairs' and other._cardsType != 'Flush Straight' and 
                    other._cardsType != 'Four Of A Kind' and other._cardsType != 'Full House' and 
                    other._cardsType != 'Flush' and other._cardsType != 'Straight' and 
                    other._cardsType != 'Three Of A Kink'):
                    return False
            elif(self._cardsType == 'One Pair' and other._cardsType != 'Flush Straight' and 
                    other._cardsType != 'Four Of A Kind' and other._cardsType != 'Full House' and 
                    other._cardsType != 'Flush' and other._cardsType != 'Straight' and 
                    other._cardsType != 'Three Of A Kink' and other._cardsType != 'Two Pairs'):
                    return False
            elif(self._cardsType == 'High Card'):
                return True
            else:
                return True               
        else:
            return False  

#test code for this class
# def main():
#    poker = Poker()
#    player = Player('Test Player1')
   
#    for i in range(1,6):
#        newCard = poker.next()
#        #newCard.showCard()
#        player.getCard(newCard)
    
    
   
#    player.showCardsInHand()


# if __name__ == '__main__':
#     main()