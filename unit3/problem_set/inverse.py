# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.
from functools import update_wrapper
def decorator(to_decorate):
    "converts function to_decorate(fn) into a decorator."
    def decorated_fn(fn):
        return update_wrapper(to_decorate(fn), fn)
    update_wrapper(decorated_fn, to_decorate) # update data for the decorator
    return decorated_fn


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

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    @trace
    def inv(y):
        left, right = 0.0, 1.0
        while f(right) < y :
            print "left ", left, " right ", right
            left, right = right, right * 2
        midpoint = (right + left) / 2
        while abs( f(midpoint) - y) > delta :
            print "***left ", left, " right ", right, "midpoint ", midpoint
            if f(midpoint) > y:
                right = midpoint
            else:
                left = midpoint
            midpoint = (right + left) / 2
        return midpoint
    return inv

def square(x): return x*x
sqrt = slow_inverse(square)
sqr = inverse(square)

#print sqrt(1000000000)
print sqr(1000000000)
