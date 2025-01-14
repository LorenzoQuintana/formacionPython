#Representación con tuplas de una baraja francesa
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Clubs", "Hearts", "Diamonds", "Spades")

deck = [(rank, suit) for rank in ranks for suit in suits]

for suit in suits:
    print(f"Suit: {suit}")
    for card in deck:
        if card[1] == suit:
            print(f"  {card[0]} of {card[1]}")
    print()

#Función que comprueba si 5 cartas son póker
def isPoker(cards):
    ranks= [card[0] for card in cards]
    for rank in ranks:
        if ranks.count(rank) == 4:
            print(f"Poker of: {rank}")
            return
    
    return print(f"There is no poker")


cards_poker = [("A", "Hearts"), ("A", "Diamonds"), ("A", "Clubs"), ("A", "Spades"), ("3", "Hearts")]
isPoker(cards_poker) 

cards_no_poker = [("A", "Hearts"), ("K", "Diamonds"), ("Q", "Clubs"), ("3", "Spades"), ("2", "Hearts")]
isPoker(cards_no_poker) 