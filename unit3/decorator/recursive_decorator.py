from functools import update_wrapper
def decorator(d):
    "Make function d a decorator: d wraps a function fn. @author Darius Bacon"
    return lambda fn: update_wrapper(d(fn), fn)

decorator = decorator(decorator)
print decorator

@decorator
def somefnc(fn):
    def funky() :
        print "Hi"
        fn()
    return funky

@somefnc
def x():
    print "Anne Hathaway"

print x
x()


