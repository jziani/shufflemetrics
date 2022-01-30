import itertools, random

def stackshuffle(deck, stack_count=5):
    """Stack shuffle: place cards from deck one by one into stack_count stacks,
    then put the stacks on top of each other to produce a new deck.

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

def riffleshuffle(deck, perfect=True):
    """Shuffle by splitting a deck in two, assemble a new deck by taking a card
    from the bottom of each stack, alternating.

    deck: an iterable to shuffle
    perfect: if True, split deck exactly in half and alternate perfectly
             between them. If False, split approximately in half adn take 1 to
             5 cards (randomly) each time.
    """

    deck = list(deck)
    midpoint = len(deck)//2
    if not perfect:
        # split the deck up to 60:40 instead of 50:50
        fuzz_factor = int(len(deck) * 0.1)
        midpoint += random.randint(-fuzz_factor, fuzz_factor)

    h1, h2 = deck[:midpoint], deck[midpoint:]

    bottom_half = h1
    r = []

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
