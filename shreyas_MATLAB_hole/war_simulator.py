import random
import matplotlib.pyplot as plt

def play_war(deck):
    # Split the deck between two players
    player1_deck = deck[::2]
    player2_deck = deck[1::2]

    # Initialize turn counter
    turn_counter = 0

    # Play the game
    while player1_deck and player2_deck and turn_counter < 1000:
        # Increase turn counter
        turn_counter += 1

        # Draw a card from each player's deck
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)

        # Take modulo 13 of the card values
        player1_card_value = (player1_card - 1) % 13 + 1
        player2_card_value = (player2_card - 1) % 13 + 1

        # Determine the winner of this round
        if player1_card_value > player2_card_value:
            player1_deck.extend([player1_card, player2_card])
        elif player2_card_value > player1_card_value:
            player2_deck.extend([player1_card, player2_card])
        else:
            player1_deck, player2_deck = war(player1_deck, player2_deck)

    # Return the number of turns taken
    return turn_counter

def war(deck1, deck2):
    # Check if there are enough cards for war
    if len(deck1) < 4 or len(deck2) < 4:
        # If one of the players doesn't have enough cards, the game ends
        return [], []

    # Draw 3 cards from each player's deck
    player1_cards = deck1[:3]
    deck1 = deck1[3:]

    player2_cards = deck2[:3]
    deck2 = deck2[3:]

    # Draw a fourth card from each player's deck
    player1_card = deck1.pop(0)
    player2_card = deck2.pop(0)

    # Take modulo 13 of the card values
    player1_card_value = (player1_card - 1) % 13 + 1
    player2_card_value = (player2_card - 1) % 13 + 1

    # Determine the winner of this war
    if player1_card_value > player2_card_value:
        deck1.extend(player1_cards + player2_cards + [player1_card, player2_card])
    elif player2_card_value > player1_card_value:
        deck2.extend(player1_cards + player2_cards + [player1_card, player2_card])
    else:
        deck1, deck2 = war(deck1, deck2)

    return deck1, deck2

# Generate a deck of cards represented as integers between 1 and 52
deck = list(range(1, 53))
random.shuffle(deck)

# Play a single game of war
turns_to_win = play_war(deck.copy())
print("Number of turns to win:", turns_to_win)

# # Simulate multiple games of war to estimate average number of turns
# n_trials = 10000
# n_turns = []
# for _ in range(n_trials):
#     deck = list(range(1, 53))
#     random.shuffle(deck)
#     n_turns.append(play_war(deck.copy()))
#
# # Plot histogram of number of turns
# plt.hist(n_turns, bins=range(1, max(n_turns) + 2), align='left', rwidth=0.8)
# plt.xlabel('Number of Turns to Win')
# plt.ylabel('Number of Games')
# plt.show()
