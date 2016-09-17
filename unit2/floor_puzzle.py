#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# Hopper does not live on the top floor.
# Kay does not live on the bottom floor.
# Liskov does not live on either the top or the bottom floor.
# Perlis lives on a higher floor than does Kay.
# Ritchie does not live on a floor adjacent to Liskov's.
# Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    # Your code here

    Hopper = Kay = Liskov = Perlis = Ritchie = None
    floors = bottom, _a, _b, _c, top =  [1, 2, 3, 4, 5]
    for hopper, kay, liskov, perlis, ritchie in list(itertools.permutations(floors)) :
        if hopper == top:
            continue
        if kay == bottom:
            continue
        if liskov == bottom or liskov == top :
            continue
        if not lives_higher(perlis, kay):
            continue
        if live_adjacent(ritchie, liskov):
            continue
        if live_adjacent(liskov, kay):
            continue

        return [hopper, kay, liskov, perlis, ritchie]

# code to represent the relationships
def lives_higher( person1, person2):
    """ returns True if person1 lives in a higher floor than person2"""
    return person1 > person2

def lives_lower( person1, person2):
    """ returns True if person1 lives in a lower floor than person2"""
    return person1 < person2

def live_adjacent( person1, person2):
    """ returns True if person1 and person2 live in adjacent floors"""
    return abs(person1 - person2 ) == 1

print floor_puzzle()
