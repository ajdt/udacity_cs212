# -----------------
# User Instructions
#
# In this problem, you will use a faster version of Pwin, which we will call
# Pwin2, that takes a state as input but ignores whether it is player 1 or
# player 2 who starts. This will reduce the number of computations to about
# half. You will define a function, Pwin3, which will be called by Pwin2.
#
# Pwin3 will only take me, you, and pending as input and will return the
# probability of winning.
#
# Keep in mind that the probability that I win from a position is always
# (1 - probability that my opponent wins).


from functools import update_wrapper

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
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


@decorator
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

goal = 40
other = {1:0, 0:1}

def hold(state):
    " applies the hold action to a given state"
    person, me , you, pending = state
    return (other[person], you, me + pending, 0)

def roll(state, dice_roll):
    " apply the given dice roll to a state"
    person, me, you, pending = state
    if dice_roll == 1 :
        return (other[person], you, me+1, 0 )
    else :
        return (person, me, you, pending + dice_roll )
def quality_of(state, action, value_function):
    "gives the expected value of doing the given action for a state using the provided value function"
    if action == 'hold' :
        return 1 - value_function(hold(state))
    elif action == 'roll' :
        return (1 - value_function(roll(state, 1))
                + sum(value_function(roll(state, d)) for d in (2,3,4,5,6))) / 6.
    else :
        raise ValueError
def possible_actions(state):
    " gives all actions possible given the argument state"
    _, _, _, pending = state
    return ["roll", "hold" ] if pending else ['roll']

def Pwin2(state):
   """The utility of a state; here just the probability that an optimal player
   whose turn it is to move can win from the current state."""
   _, me, you, pending = state
   return Pwin3(me, you, pending)

@memo
#@trace
def Pwin3(me, you, pending):
    state = (0, me, you, pending)
    if me + pending >= goal :
        return 1
    elif you >= goal :
        return 0
    else :
        return max( quality_of(state, action, Pwin2) for action in possible_actions(state) )

def test():
    epsilon = 0.0001 # used to make sure that floating point errors don't cause test() to fail
    assert goal == 40
    assert len(Pwin3.cache) <= 50000
    assert Pwin2((0, 42, 25, 0)) == 1
    assert Pwin2((1, 12, 43, 0)) == 0
    assert Pwin2((0, 34, 42, 1)) == 0
    assert abs(Pwin2((0, 25, 32, 8)) - 0.736357188272) <= epsilon
    assert abs(Pwin2((0, 19, 35, 4)) - 0.493173612834) <= epsilon
    return 'tests pass'

print Pwin2((0, 25, 32, 8)) - 0.736357188272
print test()
