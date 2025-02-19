card_deck = input().split()
shuffles = int(input())

small_deck = card_deck[1:-1]
half_deck = int(len(small_deck) / 2)

temp_deck = []

for i in range(shuffles):
    for x, y in zip(small_deck[:half_deck], small_deck[half_deck:]):
        temp_deck += [y, x]
    small_deck = temp_deck
    temp_deck = []

card_deck[1:-1] = small_deck

print(card_deck)
