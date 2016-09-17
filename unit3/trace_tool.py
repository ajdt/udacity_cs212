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

# we'll be doing a trace on the fibonacci function naive implementation
@trace
def fib(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib(6)
