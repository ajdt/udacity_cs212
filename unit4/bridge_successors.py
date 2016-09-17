# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.
import itertools

#### FROM UNIT 3, for debugging only
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
def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here :
        successors, arrow = move_people(here, there, t), '->'
    else:
        successors, arrow = [ (l, r, t, s ) for r, l, t, s in move_people(there, here, t)], '<-'
    return dict( [ [(here, there, time),  tuple(list(selected) + [arrow]) ]
                    for here, there, time, selected in successors])

    # my more verbose way of forming the dictionary
    #dictionary = {}
    #for here, there, time, selected in successors :
    #    action = tuple(list(selected) + [arrow])
    #    dictionary[(here, there, time)] = action
    #return dictionary




@trace
def move_people(send_from, send_to, time, token="light"):
    """ Returns a list of all possible states that
    could result from moving any one or two people from
    the set send_from to the set send_to. Removes
    the token argument from send_from and adds it to
    send to. Each state returned has the form:
        (send_from, send_to, time, (selected_people))
    where selected_people is a tuple of the people
    having crossed ( one person listed twice if only
    one crosses)"""
    send_from = send_from.difference([token])
    send_to = send_to.union([token])
    candidates = [ set(x) for x in set(itertools.combinations(send_from, 2)).union(
                       set(itertools.combinations(send_from, 1)))]
    return [ (send_from.difference(pair), send_to.union(pair), time + max(pair),
                (tuple(pair) if len(pair) > 1 else tuple(pair)*2) )
                  for pair in candidates]

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'

print test()



# PETER NORVIG's solution

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here :
        return dict(((here - frozenset([a, b, 'light']),
            there | frozenset([a, b, 'light']),
            t + max(a, b)),
            (a, b, '->'))

            for a in here if a is not 'light'
            for b in here if b is not 'light'
            )
    else:
        return dict(((here | frozenset([a, b, 'light']),
            there - frozenset([a, b, 'light']),
            t + max(a, b)),
            (a, b, '<-'))

            for a in here if a is not 'light'
            for b in here if b is not 'light'
            )

# I think Norvig is guilty of violating DRY a little
# too much with that code

# but I'm guilty of overcomplicating my solution. There's
# no reason to use the itertools module, when a set of
# nested for loops does the same thing, likewise the way
# he builds his dictionary is very concise, and doesn't
# make  use of any intermediate forms like the one
# returned by my helper function move_people()
# see improved_bridge_successors.py for my attempt to make
# my solution more efficient
