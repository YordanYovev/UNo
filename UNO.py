import random







def buildDeck ():
    deck = []
    colours = ["Red", "Green", "Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]
    wilds = ["Wild","Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = "{} {} ".format(colour, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    # print(deck)
    # print(len(deck))

    return deck

#shuffles.Trying to make a function instead of using only shuffle function from random
#import random still need it

def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

#Draw card function

def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(UNOdeck.pop(0))
    return cardsDrawn

#print formated list of player hand

def showHand(player,playerHand):
    print("player {}".format(player+1))
    print("Your hand:")
    print("-------------------")
    y=1
    for card in playerHand:
        print("{}) {}".format(y, card))
        y +=1
    print("-------------------")

#check if player is able to play a card
def canPlay(colour,value,playerHand):
    for card in playerHand:
        if "Wild" in card:  #splitCard[-1]:
            return True
        elif colour in card or value in card:
            return True
    return False


UNOdeck = buildDeck()
UNOdeck = shuffleDeck(UNOdeck)
# print(UNOdeck)
# print("***********************")
random.shuffle(UNOdeck) #<-------just for fun extra shuffle
# print(UNOdeck)
discard = []
# pl1=""
# pl2=""
# pl3=""
# pl4=""
players = []
numPlayers = int(input("How many players?"))


# playersNames = numPlayers    #working proces
# if playersNames == 2:
#     pl1=input("Plaese enter your name:")

while numPlayers <2 or numPlayers>4:
    numPlayers = int(input("Invalid!!! Plaese enter number between 2-4.How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))


colours = ["Red", "Green", "Yellow","Blue"]
# print(players)

playerTurn = 0
playDirection = 1
playing = True
discard.append(UNOdeck.pop(0))
splitCard = discard[0].split(" ",1)
currentColour = splitCard[0]

if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    showHand(playerTurn,players[playerTurn])
    print("Card on the top of discard deck: {}".format(discard[-1]))
    if canPlay(currentColour,cardVal,players[playerTurn]):
        cardChosen = int(input("Which card do you want to play?"))
        while not canPlay(currentColour,cardVal,[players[playerTurn][cardChosen -1]]):
            cardChosen = int(input("Not a valid card.Which card do you want to play?"))
        print("You played : {}".format(players[playerTurn][cardChosen -1]))
        print("*****")
        discard.append(players[playerTurn].pop(cardChosen-1))

            #check for special cards   <------------------------- problem
        splitCard = discard[-1].split(" ",1)
        currentColour = splitCard[0]
        if len(splitCard) == 1:
            cardVal = "Any"
        else:
            cardVal = splitCard[1]
        if currentColour == "Wild":
            for x in range(len(colours)):
                print("{}) {}".format(x+1, colours[x]))
            newColour = int(input("What colour you would like to choose?"))
            while newColour < 1 or newColour > 4:
                newColour = int(input("Invalid option.What colour you would like to choose?"))
            currentColour = colours[newColour - 1]
        if cardVal == "Reverse":
            playDirection = playDirection * -1
        elif cardVal == "Skip":
            playerTurn += playDirection
            if playerTurn >= numPlayers:
                playerTurn = 0
            elif playerTurn < 0:
                playerTurn = numPlayers -1
        elif cardVal == "Draw Two":
            playerDraw = playerTurn + playDirection
            if playerDraw == numPlayers:
                playerDraw = 0
            elif playerTurn < 0:
                playerDraw = numPlayers -1
            players[playerTurn].extend(drawCards(2))
        elif cardVal == "Draw Four":
            playerDraw = playerTurn + playDirection
            if playerDraw == numPlayers:
                playerDraw = 0
            elif playerTurn < 0:
                playerDraw = numPlayers -1
            players[playerTurn].extend(drawCards(4))
        print("-------------------")
    else:
        print("You cant play. You have to draw a card")
        players[playerTurn].extend(drawCards(1))





    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers -1
