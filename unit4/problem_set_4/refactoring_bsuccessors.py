# -----------------
# User Instructions
#
# In this problem you will be refactoring the bsuccessors function.
# Your new function, bsuccessors3, will take a state as an input
# and return a dict of {state:action} pairs.
#
# A state is a (here, there, light) tuple. Here and there are
# frozensets of people (each person is represented by an integer
# which corresponds to their travel time), and light is 0 if
# it is on the `here` side and 1 if it is on the `there` side.
#
# An action is a tuple of (travelers, arrow), where the arrow is
# '->' or '<-'. See the test() function below for some examples
# of what your function's input and output should look like.


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

@trace
def bsuccessors3(state):
    """Return a dict of {state:action} pairs.  State is (here, there, light)
    where here and there are frozen sets of people, light is 0 if the light is
    on the here side and 1 if it is on the there side.
    Action is a tuple (travelers, arrow) where arrow is '->' or '<-'"""
    here_op, there_op, select_set, arrow,new_light = get_set_operations(state)

    pairs = [ [(here_op(frozenset([a,b])), there_op(frozenset([a,b])), new_light),
        (frozenset([a, b]), arrow)]
      for a in select_set for b in select_set ]

    return dict(pairs)

def get_set_operations(state):
    """Returns several arguments related to finding bsuccessors.
    h_op and t_op are two lambda's. They take a frozenset()
    of selected people, and return the correct set values
    for here and there respectively. choices represents
    the set to choose candidates from, arrow is an action
    string, and new_light is the new value for light"""
    here, there, light = state
    choices, new_light, arrow = ( (here, 1, '->') if not light else (there, 0, '<-'))

    h_op = lambda remove_set: lambda s: remove_set - s
    t_op = lambda union_set: lambda s: union_set | s
    if light :
        h_op, t_op = t_op, h_op
    return h_op(here), t_op(there), choices, arrow, new_light


def test():
    assert bsuccessors3((frozenset([1]), frozenset([]), 0)) == {
            (frozenset([]), frozenset([1]), 1)  :  (set([1]), '->')}

    assert bsuccessors3((frozenset([1, 2]), frozenset([]), 0)) == {
            (frozenset([1]), frozenset([2]), 1)    :  (set([2]), '->'),
            (frozenset([]), frozenset([1, 2]), 1)  :  (set([1, 2]), '->'),
            (frozenset([2]), frozenset([1]), 1)    :  (set([1]), '->')}

    assert bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1)) == {
            (frozenset([2, 4, 5]), frozenset([3]), 0)   :  (set([5]), '<-'),
            (frozenset([2, 3, 4, 5]), frozenset([]), 0) :  (set([3, 5]), '<-'),
            (frozenset([2, 3, 4]), frozenset([5]), 0)   :  (set([3]), '<-')}
    return 'tests pass'

print test()


# NORVIG's solution
# as typical, Norvig came up with a very nice and simple
# solution. Because he chose a good representation for light
# the solution is quite concise:

# def bsuccessors3(state):
#    _, _, light = state
#    return dict( bsuccessor3(state, set([a,b]))
#            for a in state[light]
#                for b in state [light])
#
#
#def bsuccessor3(state, travelers):
#    " The single successor state when this set of travelers move."
#    _, _, light = state
#    start = state[light] | travelers
#    dest = state [1 - light ] | travelers
#    if light == 0:
#        return (start, dest, 1), (travelers, '->')
#    else:
#        return (dest, start, 0), (travelers, '<-')

# using light as an index makes a lot of things more concise
