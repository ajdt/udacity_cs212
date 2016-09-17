# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars).

def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null

# MY CODE HERE...
def alt(x, y):      return lambda Ns: set( [ i for i in x(Ns) ] + [ j for j in y(Ns)])
# Norvig's version : "lambda Ns: x(Ns) | y(Ns)"


def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky

# MY CODE HERE...
def oneof(chars):   return lambda Ns: set( [ x for x in chars if 1 in Ns ])
# Norvig's solution : "lambda Ns: set(chars) if 1 in Ns else None"
# Norvig's code seems much simpler. I have the
# right idea, but my code lacks elegance


def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.

null = frozenset([])

def test():

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    return 'tests pass'
