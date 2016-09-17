from functools import update_wrapper

def decorator(f):

    def decorated_f(fn):
        return update_wrapper(f(fn), fn)

    update_wrapper(decorated_f, f)
    return decorated_f


#@decorator
def call_eight_times(fn):
    def fn_edited():
        for i in range(0,8):
            fn()
    return fn_edited

@call_eight_times
def print_text():
    print "Here's johnny"

print_text()
