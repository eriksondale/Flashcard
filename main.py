# NEED TO:
# Determine appropriate data structure to use
# Command-line arguments
# GUI (later)
# Want to add support for multiple decks at same time

#Format
# tab delimitted (front, back, know(0,1))
# .fc (flash card)

class Card:
    # Card properties
    def __init__(self, id, quest, ans):
        self.id = id # ID variable, determined by deck class 
        self.quest = quest # question variable
        self.ans = ans # answer variable
        self.knowIt = 0
    def changeQuest(self, quest): #Change Values
        self.quest = quest
    def changeAns(self, ans):
        self.ans = ans
    def changeKnow(self, knowIt):
        self.knowIt = knowIt
    def getQuest(self): # Read Values
        return self.quest
    def getAns(self):
        return self.ans
    def getKnow(self):
        return self.knowIt



class Deck: # DS is TBD
    def __init__(self):
        self.deck = [] # initialize empty list
    def shuffle(self): # Shuffle deck, what's an efficient algorithm for this?
        pass
    def add(self, myCard): # Add Card to Deck
        self.deck.append(myCard)
    def remove(): # Remove Card from Deck
        pass
    def dump(self): # Outputs all Deck Info
        for tempCard in self.deck:
            print(tempCard.getQuest() + "\n" + tempCard.getAns() + "\n\n")


print('Starting....')


while(True):
    print('Options: ')
    print('1. Import Deck') # Assume .fc
    print('2. Export/Save Deck') # Assume .fc
    print('3. Add Card')
    print('4. Edit Card') # Just use add, remove functions?
    print('5. Remove Card')
    print('6. Quiz All')
    print('7. Quiz Missed')
    print('8. Exit')
    print('0. Admin Info')
    usrIn = input('>')
    if(usrIn == 1): # Import Deck Function
        # enter .fc (flash card) file
        # try
            # open file
            # for line in file
            # split based on \t
            # construct card object
            # add card object to Deck DS
        # except
            # print error reading file
        pass
    if(usrIn == 3):
        myDeck = Deck()
        tempQuest = raw_input("Enter one side of card: ")
        tempAns = raw_input("Enter other side of card: ")
        tempCard = Card(tempQuest, tempAns)
        myDeck.add(tempCard)
        print("Added Card!")
    if(usrIn == 5): # Remove Card
        # sort cards by ID
        # List card ID and select to remove
    if(usrIn == 6):
        # shuffle()
        # subloop and quiz
        pass
    if(usrIn == 7):
        # Make separate list with know==0 and shuffle()
        # subloop and quiz
        pass
    if(usrIn == 8):
        break
    if(usrIn == 0):
        myDeck.dump()
