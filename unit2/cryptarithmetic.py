# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.

import string, re, itertools
# Norvig likes the design of each program b/c the
# functions are all simple in design

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


# fill_in function is a generator so we don't go through all the answers
# we can stop early, as soon as a valid one is found
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = "".join( [x for x in string.ascii_letters if string.find(formula, x) != -1 ])
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

# valid could almost be one line, just the eval,
# but by breaking it out into a separate function
# we can have separate checks for leading 0s and catch
# arithmetic exceptions

def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
