# -----------------
# User Instructions
#
# In this problem, we introduce doubling to the game of pig.
# At any point in the game, a player (let's say player A) can
# offer to 'double' the game. Player B then has to decide to
# 'accept', in which case the game is played through as normal,
# but it is now worth two points, or 'decline,' in which case
# player B immediately loses and player A wins one point.
#
# Your job is to write two functions. The first, pig_actions_d,
# takes a state (p, me, you, pending, double), as input and
# returns all of the legal actions.
#
# The second, strategy_d, is a strategy function which takes a
# state as input and returns one of the possible actions. This
# strategy needs to beat hold_20_d in order for you to be
# marked correct. Happy pigging!

import random

def trace(fn) :
    """ decorator that traces a function fn, displaying data for each function call
    and return from a function call"""
    indent = "    " # space for one indentation
    trace.stack_depth = 0

    def traced_fn(*args):

        # print call data
        signature = "%s(%s)" % (fn.__name__, ", ".join(map(repr, args)))
        print "%s-->%s" % (indent*trace.stack_depth, signature )
        trace.stack_depth += 1
        result = fn(*args)

        # print the results
        print "%s<--%s == %s" % (indent*trace.stack_depth, signature, result)
        trace.stack_depth -= 1

        return result   # must return the same result as the traced function
    return traced_fn


def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args refuses to be a dict key
            return f(args)
    _f.cache = cache
    return _f


def pig_actions_d(state):
    """The legal actions from a state. Usually, ["roll", "hold"].
    Exceptions: If double is "double", can only "accept" or "decline".
    Can't "hold" if pending is 0.
    If double is 1, can "double" (in addition to other moves).
    (If double > 1, cannot "double").
    """
    # state is like before, but with one more component, double,
    # which is 1 or 2 to denote the value of the game, or 'double'
    # for the moment at which one player has doubled and is waiting
    # for the other to accept or decline
    (p, me, you, pending, double) = state
    if double == 'double' :
        return [ 'accept', 'decline' ]
    actions = ['roll']
    if pending != 0 :
        actions.append('hold')
    if double == 1 :
        actions.append('double')

    return actions




## You can use the code below, but don't need to modify it.

def hold_20_d(state):
    "Hold at 20 pending.  Always accept; never double."
    (p, me, you, pending, double) = state
    return ('accept' if double == 'double' else
            'hold' if (pending >= 20 or me + pending >= goal) else
            'roll')

def clueless_d(state):
    return random.choice(pig_actions_d(state))

def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)

def play_pig_d(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0, 1)
    while True:
        (p, me, you, pending, double) = state
        if me >= goal:
            return strategies[p], double
        elif you >= goal:
            return strategies[other[p]], double
        else:
            action = strategies[p](state)
            state = do(action, state, dierolls)

## No more roll() and hold(); instead, do:

def do(action, state, dierolls):
    """Return the state that results from doing action in state.
     If action is not legal, return a state where the opponent wins.
    Can use dierolls if needed."""
    (p, me, you, pending, double) = state
    if action not in pig_actions_d(state):
        return (other[p], goal, 0, 0, double)
    elif action == 'roll':
        d = next(dierolls)
        if d == 1:
            return (other[p], you, me+1, 0, double) # pig out; other player's turn
        else:
            return (p, me, you, pending+d, double)  # accumulate die in pending
    elif action == 'hold':
        return (other[p], you, me+pending, 0, double)
    elif action == 'double':
        return (other[p], you, me, pending, 'double')
    elif action == 'decline':
        return (other[p], goal, 0, 0, 1)
    elif action == 'accept':
        return (other[p], you, me, pending, 2)

goal = 40
other = {1:0, 0:1}
def hold(state):
    person, me, you, pending, double = state
    return (other[person], you, me+pending, 0, double)
def roll(state, d):
    person, me, you, pending, double = state
    if d == 1:
        return (other[person], you, me+1, 0, double)
    else:
        return (person, me, you, pending+d, double)


def action_value(state, action):
    person, me, you, pending, double = state
    if action == 'decline':
        return -1*state_value((other[person], goal, 0, 0, 1  ) )
    if action == 'accept':
        return -1*state_value((other[person], you, me, pending, 2))
    if action == 'double':
        return -1*state_value((other[person], you, me, pending, 'double'))
    if action == 'hold' :
        return state_value( (other[person], you, me+pending, 0, double))
    if action == 'roll':
        return (-1*state_value( (other[person], you, me+1, 0, double))+
                sum( state_value((person, me, you, pending+d, double)) for d in range(2,7)))/6
    raise ValueError

@memo
#@trace
def state_value(state):
    p, me, you, pending, double = state
    if double == 'double':
        double = 1
    if me + pending >= goal :
        return 1.0*double
    if you >= goal:
        return -1.0*double
    def value_for_state(a): return action_value(state, a)
    return max(map( value_for_state, pig_actions_d(state) ))

#@trace
def strategy_d(state):
    def value_for_action(a): return action_value(state, a)
    #print pig_actions_d(state)
    #print map(value_for_action, pig_actions_d(state))
    return max( pig_actions_d(state), key=value_for_action)

def simple_strategy(state):
    person, me, you, pending, double = state
    if double == 'double' :
        if you - me < 10 :
            return 'accept'
        else:
            return 'decline'
    if me - you > 5 and double == 1:
        return 'double'
    if pending >= 20 or me + pending >= goal :
        return 'hold'
    return 'roll'

def strategy_compare(A, B, N=1000):
    """Takes two strategies, A and B, as input and returns the percentage
    of points won by strategy A."""
    A_points, B_points = 0, 0
    for i in range(N):
        if i % 2 == 0:  # take turns with who goes first
            winner, points = play_pig_d(A, B)
        else:
            winner, points = play_pig_d(B, A)
        if winner.__name__ == A.__name__:
            A_points += points
        else: B_points += points
    A_percent = 100*A_points / float(A_points + B_points)
    print 'In %s games of pig, strategy %s took %s percent of the points against %s.' % (N, A.__name__, A_percent, B.__name__)
    return A_percent

def test():
    assert action_value (( 1, 38, 4, 0, 1), 'double') > 0

    assert set(pig_actions_d((0, 2, 3, 0, 1)))          == set(['roll', 'double'])
    assert set(pig_actions_d((1, 20, 30, 5, 2)))        == set(['hold', 'roll'])
    assert set(pig_actions_d((0, 5, 5, 5, 1)))          == set(['roll', 'hold', 'double'])
    assert set(pig_actions_d((1, 10, 15, 6, 'double'))) == set(['accept', 'decline'])

    assert state_value( (0, goal, 5, 0, 2)) == 2
    assert state_value( (0, goal, 5, 0, 1)) == 1
    assert state_value( (0, 0, goal, 0, 2)) == -2
    assert state_value( (0, 0, goal, 0, 1)) == -1
    assert state_value( (1, 35, 35, 7, 1)) == 1

    print strategy_compare(simple_strategy, hold_20_d ) > 60 # must win 60% of the points
    return 'test passes'

print test()
#test()
#print  state_value.cache
#for k, v in state_value.cache.items():
#    print k, " ", v


