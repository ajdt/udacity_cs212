import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    # shuffle the deck
    random.shuffle(deck)
    hands = []
    if len(deck) < (numhands*n):
        return None
    for i in range(0, numhands):
        new_hand = []
        for i in range(0, n):
            new_hand.append(deck.pop())
        hands.append(new_hand)
    return hands

print deal(3)
