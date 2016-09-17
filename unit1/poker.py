# NOTE: Most of the code in this file is my more verbose implementations
# of the same functions delineated by Prof. Norvig in the udacity course
# CS 212 "Design of Computer Programs"
# a few functions have been copied verbatim, where this happens I have
# indicated as such



# From video 24
# -----------
# User Instructions
#
# Write a function, allmax(iterable, key=None), that returns
# a list of all items equal to the max of the iterable,
# according to the function specified by key.

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    max_value = max(iterable, key=key)
    max_list = []
    for i in iterable:
	# my code requires checking for a key, prof's code uses a lambda instead
        if key == None and i == max_value :
            max_list.append(i)
        if key != None and key(i) == key(max_value) :
            max_list.append(i)
    return max_list

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

# -----------
# User Instructions
#
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    # This is my verbose solution to the straight() function
    descending = True
    sorted_ranks = sorted(ranks)
    for i in range(1, len(ranks)) :
        if sorted_ranks[i] != (sorted_ranks[i - 1] + 1 ) :
            descending = False
    return descending

def flush(hand):
    "Return True if all the cards have the same suit."
    # this is my verbose solution to the flush() function
    suit_list = []
    for rank, suit in hand:
        suit_list.append(suit)
    return (len(set(suit_list)) == 1)

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # This is my naive implementation
    # a shorter solution involves using the list function
    # "count" which counts the number of occurrences of a value
    # within a list!!!
    same_type_count = 1
    kind_rank = None
    ranks.sort(reverse = True )
    sorted_hand = ranks


    for i in range(1, len(sorted_hand)):
        print "comparing ", i, " to ", i - 1, " same type count: ", same_type_count
        if sorted_hand[i] == sorted_hand[i-1]:
            same_type_count += 1
        elif same_type_count == n : # n-kind is found, before current hand
            kind_rank = sorted_hand[i - 1]
            break
        else:
            same_type_count = 1

        # last card makes up part of n-kind
        if i == (len(sorted_hand) - 1) and same_type_count == n :
            kind_rank = sorted_hand[i]
    return kind_rank

def card_ranks(hand):
    # this implementation is provided by Prof. Norvig
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    fkranks = card_ranks(fk)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'
    return 'tests pass'

print test()
