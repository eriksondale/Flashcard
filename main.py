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

class Deck: # DS is TBD
    def shuffle(self): # Shuffle deck
        pass
    def add(): # Add Card to Deck
        pass
    def remove(): # Remove Card from Deck
        pass
    def dump(): # Outputs all Deck Info
        pass


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
    if(usrIn == 7):
        break
