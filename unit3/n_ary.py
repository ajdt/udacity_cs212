# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function.

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # base cases
        if args == None or len(args) == 0:
            return x
        if len(args) == 1:
            return f(x, args[0])
        else:
            # must not forget to unpack the arguments
            # before passing them along, otherwise
            # the rest of the tuple is considered
            # to be one argument
            return f(x, n_ary_f(args[0], *args[1:]))
    return n_ary_f

def seq(x, y):
    return ('seq', x, y)

nary_seq = n_ary(seq)

print nary_seq('a', 'b', 'c', 'd', 'e', 'f')


# Norvig's solution:

def n_ary(f):

    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f


# Notice why his solution is much more elegant!!!!
# he doesn't split up the list manually, instead
# relying on the fact that the call to n_ary_f will
# automatically match the arguments to x and *args
#
# He also doesn't have a base case for len(args) == 1
# b/c this is reducible to the base case where there
# are no args and we just return x.
#
# His usage of the expression "if not args"
# shows a greater mastery of the language
# I didn't even consider such an expression


# Lessons learned:
# know your language better
# look more closely for violations of DRY,
# Norvig is concise b/c he's reusing code even within this
# function.

# Knowing the language better also comes into play b/c
# the nature of this solution is beyond what I could come
# up with. I'm not used to thinking of functions as first
# class values
