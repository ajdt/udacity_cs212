# NOTE: this file only contains the lines that
# were optimized, see oneof_and_alt.py for a
# complete listing of source code.


# It's wasteful to compute the set of s every time
# our function gets called, since we know what s is
# at compile time, and we don't do any calculation on it
def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null

# the code becomes...
def lit(s):
    set_s = set([s])
    return lambda Ns: set_s if len(s) in Ns else null

# thus we've extracted out a computation that was happening
# with each call, but only needed to happen once. This is
# an advantage of having a compiler, we can do certain
# things only once instead of having to do them repeatedly





#  Likewise the following ...
def oneof(chars): return lambda Ns: set(chars) if 1 in Ns else None

# ... gets transformed to
def oneof(chars):
    char_set = set(chars)
    return lambda Ns: char_set if 1 in Ns else None


