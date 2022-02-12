import copy
import shuffle, visualize
import nltk.nltk as nltk

num_cards = 25

html = [visualize.header, "<h2>An unshuffled deck:</h2>"]

deck = list(zip(range(num_cards), visualize.make_hues(num_cards)))# tuples: (card_id, hue))
original_deck = copy.deepcopy(deck)

html.append(visualize.hues2html([card[1] for card in deck]))
html.append('<p>Jaro similarity with unshuffled deck: {}</p>'.format(nltk.jaro_similarity(deck, original_deck)))
html.append('<p>Jaro-Mallory similarity with unshuffled deck: {}</p>'.format(nltk.jaro_mallory_similarity(deck, original_deck)))

html.append("<h2>after a riffle shuffle:</h2>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))
html.append('<p>Jaro similarity with unshuffled deck: {}</p>'.format(nltk.jaro_similarity(deck, original_deck)))
html.append('<p>Jaro-Mallory similarity with unshuffled deck: {}</p>'.format(nltk.jaro_mallory_similarity(deck, original_deck)))

html.append("<h2>after another riffle shuffle:</h2>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))
html.append('<p>Jaro similarity with unshuffled deck: {}</p>'.format(nltk.jaro_similarity(deck, original_deck)))
html.append('<p>Jaro-Mallory similarity with unshuffled deck: {}</p>'.format(nltk.jaro_mallory_similarity(deck, original_deck)))

html.append("<h2>after third riffle shuffle:</h2>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))
html.append('<p>Jaro similarity with unshuffled deck: {}</p>'.format(nltk.jaro_similarity(deck, original_deck)))
html.append('<p>Jaro-Mallory similarity with unshuffled deck: {}</p>'.format(nltk.jaro_mallory_similarity(deck, original_deck)))

html.append("<h2>after fourth riffle shuffle:</h2>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))
html.append('<p>Jaro similarity with unshuffled deck: {}</p>'.format(nltk.jaro_similarity(deck, original_deck)))
html.append('<p>Jaro-Mallory similarity with unshuffled deck: {}</p>'.format(nltk.jaro_mallory_similarity(deck, original_deck)))

html.append(visualize.footer)
print(''.join(html))

