from poker import Poker
from card import Card
from player import Player

def main():
    #create a poker object
    thePoker = Poker()
    #shuffle this poker
    thePoker.shuffle()
    for cards in thePoker.cards :
        cards.makeShowCase()
    #create a rule object
    #texasHoldem = Rule()
    #create new players
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    #for _ in range(5):
    for i in range(0,5):
        for player in players:
            player.getCard(thePoker.next())
            print("Cards before arrange: ")
            player.showCardsInHand()
            print("")
    #newArr = sorted(players,reverse=True)           
    
    for player in players:
         #: arrange players' cardsInHand
        player.arrange()
        print("Cards after arrange: ")
        player.showCardsInHand()
        player.findType()
        player.ifFlushStraight()
        print("")
    
    
    newArr = sorted(players,reverse=True)
    
    for i in newArr:    
        print(i.name + ': '+i._cardsType, end=' ' + '\n')       
        i.showCardsInHand()

    print('\n' + 'Winner is: ' + newArr[0].name + 'with ' + newArr[0]._cardsType )
        

        

        


if __name__ == '__main__':
    main()