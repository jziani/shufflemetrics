import shuffle, visualize

num_cards = 25

html = [visualize.header, "<p>An unshuffled deck:</p>"]

deck = list(zip(range(num_cards), visualize.make_hues(num_cards)))# tuples: (card_id, hue))

html.append(visualize.hues2html([card[1] for card in deck]))

html.append("<p>after a riffle shuffle:</p>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))

html.append("<p>after another riffle shuffle:</p>")
deck = shuffle.riffleshuffle(deck)
html.append(visualize.hues2html([card[1] for card in deck]))

html.append(visualize.footer)
print(''.join(html))

