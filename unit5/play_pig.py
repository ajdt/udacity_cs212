# -----------------
# User Instructions
#
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy. Enter your code at line 41.
#
# You may want to borrow from the random module to help generate die rolls.

import random

possible_moves = ['roll', 'hold']
other = {1:0, 0:1}
goal = 50

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def play_pig(A, B):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    state, strategies, current_player = (0, 0, 0, 0), (A, B), 0
    while state[current_player+1] < goal :
        current_player = state[0]
        if strategies[current_player](state) == 'roll':
            state = roll(state, random.randint(1,6) )
        else:
            state = hold(state)
    # current_player references last player who's score changed
    # which is the winning player
    return strategies[current_player]

# My above solution sacrifices clarity for brevity a little
# too much, it's not easily apparent that current_player
# references the winning player at the end, though this is true

# it's also hard to tell that the loop condition accesses
# the current player's score

# Norvig's version

# strategies = [A, B]
# state = (0, 0, 0, 0)

# while True:
#   (p, me, you, pending) = state
#    if me >= goal:
#        return strategies[p]
#    elif you >= goal:
#        return strategies[other[p]]
#    elif strategies[p](state) == 'hold':
#        state = hold(state)
#    else:
#        state = roll(state, random.randint(1,6))

# I like Norvig's solution b/c it's clear and it uses
# the if/else construct for two purposes: to return the
# correct value, and to check if anyone has won yet.

# an earlier implementation I had, checked if anyone had
# won in the loop condition, and further down checked who
# it was, to return the correct value


def always_roll(state):
    return 'roll'

def always_hold(state):
    return 'hold'

def test():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'
    return 'tests pass'

print test()


