"""This file implements several shuffling techniques. For descriptions of
the different types of shuffle, see https://en.wikipedia.org/wiki/Shuffling

These function simulate how I personally shuffle my deck when playing Dominion,
a game where deck sizes vary over the course of the game and usually contain at
least 10 cards. The constants ("magic numbers") in these functions and the
specifics of the algorithms stem from how I shuffle in real life and are not
intended to be "fair" or "truly random" or anything like that.
"""

import itertools, random

def stackshuffle(deck, stack_count=5):
    """Stack shuffle: place cards from deck one by one into stack_count stacks,
    then put the stacks on top of each other to produce a new deck.

    This is also called pile shuffling.

    deck: an iterable to shuffle
    stack_count: how many stacks to split the deck into
    repetitions: repeat this shuffle this many times
    """

    stacks = []
    for _ in range(stack_count):
        stacks.append([])

    for n, card in enumerate(deck):
        stacks[n%stack_count].append(card)

    r = []
    for s in stacks:
        r.extend(s)

    return r

def riffleshuffle(deck, perfect=False):
    """Shuffle by splitting a deck in two, assemble a new deck by taking a card
    from the bottom of each stack, alternating.

    deck: an iterable to shuffle
    perfect: if True, split deck exactly in half and take one card at a time alternating
             between the halves while riffling. If False, split the deck
             approximately in half and take 1 to several cards from each half
             while riffling.
    """

    deck = list(deck)
    midpoint = len(deck)//2
    if not perfect:
        # split the deck up to 60:40 instead of 50:50
        fuzz_factor = int(len(deck) * 0.1)
        midpoint += random.randint(-fuzz_factor, fuzz_factor)

    h1, h2 = deck[:midpoint], deck[midpoint:]

    bottom_half = h1
    r = [] # The shuffled deck

    while len(h1) or len(h2):
        r.append(bottom_half.pop())

        if not perfect:
            count = min(random.randint(0,3), len(bottom_half))
            for _ in range(count):
                r.append(bottom_half.pop())

        if bottom_half is h1 and len(h2) > 0:
            bottom_half = h2
        elif len(h1) > 0:
            bottom_half = h1

    return r

def overhand(deck):
    """Shuffle by pulling a clump of cards from the middle of the deck. From
    this clump, take a few cards off the top of the clump and put them on top
    of the deck. Repeat.
    """

    deck = list(deck)

    # Pull a clump of cards from the middle of the deck
    clump_top = random.randint(1, len(deck)//2)
    clump_bottom = random.randint(clump_top+1, len(deck)-1)

    clump = deck[clump_top:clump_bottom]
    deck = deck[:clump_top] + deck[clump_bottom:]

    # Picking a few cards at a time, place cards from clump on top of deck
    while clump:
        how_many = random.randint(1, min(len(clump), 5))
        for _ in range(how_many):
            deck.insert(0, clump.pop())

    return deck


def repeat(n, function, deck):
    """Shuffle a deck n times with a particular shuffle function.

    Does not support function args other than deck
    """

    for _ in range(n):
        deck = function(deck)

    return deck

