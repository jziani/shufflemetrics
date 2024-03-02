import numpy as np
from textwrap import wrap
import random
import math

## We implement best deck as a global variable to keep things simple, since the best deck is in fact deterministic

class BestDeck:
    L = 0
    H = 0
    for i in range(52):
        H += (i+1) * 10**(2*i-1)
        L += (52-i) * 10**(2*i-1)
        
    def __init__(self, val = '01250603280833482939243622151242493826184021173752323011162041090534194604501043020731514514444735232713', low = L, high = H): 
        self.val = val
        self.low = low 
        self.high = high

## Below, we implement a function that computes the best deck, representing it as a list
    def best_deck(self):
        str_val = self.val
        str_list = wrap(str_val, 2)
        val_list = [int(char) for char in str_list]

        return val_list 
        
## Below, we implement a function that computes the l1 distance between any deck and the best deck
    def distance(self, deck):
        return np.sum(np.abs(np.array(deck) - np.array(self.best_deck())))
    
## We provide the hash/key representation of a deck below. This is the inverse shuffle function
    def key(self, deck):
        x = 0
        for i in range(52):
            x += deck[i] * 10**(2*i-1)   
        return (x - self.low)/(self.high - self.low)
    
## TO DO: key_to_dect() function that gives the deck given a key

    
    
## We provide example use cases of the best_deck utility functions below, both on the best deck and on a random deck:
BestDeck = BestDeck()
best_deck = BestDeck.best_deck()
rand_deck = list(range(1,53))
random.shuffle(rand_deck)

# Telling people how lovely the best deck is: 
print('This is the loveliest deck in the history of decks: {}'.format(BestDeck.best_deck()))  


# Printing the  distance of a random deck to the best deck
print('We generated a random deck that has l1-distance {} to the best deck'.format(BestDeck.distance(rand_deck)))
#print('This is, by the way, the random deck: {}'.format(rand_deck))

#Print the inverse 
print('The best deck has key {}'.format(BestDeck.key(best_deck)))
print('Our random deck has key {}'.format(BestDeck.key(rand_deck)))

  

