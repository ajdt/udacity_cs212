# -----------------
# User Instructions
#
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either
# return 'roll' or 'hold'). Take a look at the random library for
# helpful functions.

import random

possible_moves = ['roll', 'hold']

random.seed()
def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return possible_moves[ random.randint(0, len(possible_moves) - 1) ]

# A better way is to
# use random.choice(sequence)
# where a random choice is returned from the input
# sequence. This is what Norvig did

# ALWAYS LOOK @ WHAT THE LANGUAGE OFFERS BEFORE CODING!!!!

