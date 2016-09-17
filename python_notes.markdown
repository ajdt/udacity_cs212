NOTE: CREATE A SYMBOL LIST FOR PYTHON !!!!!!!!!!!!!!
* go through learn python the hard way, list of python keywords
    pg 120 , Exercise 37
* better notes on array slicing, better notes on list comprehensions

User input
====================
* use raw_input([prompt])   in python 2
* use input([prompt])       in python 3
    > in either case the prompt is optional i.e. can use input() 

printing text
====================
    > use the "print" function
    > put a comma at the end of last argument to print, to suppress '\n' 
    ex:     print "hi there " + name,
                print "how are you doing?"
    > to print a mixture of strings and numbers, separate each argument
    via a comma :
        print "I have ", 3 * 3, " hens."        => "I have 9 hens."
    > STRING INTERPOLATION
        > use a % format string similar to C's printf function
        > ex: print " I have %i hens" % num_hens
        > ex2: print "My name is %s and I have %i hens" %(name, num_hens) 
        > %r is a useful format character ???
    > Printing a string verbatim:
        > use the delimiter """ to fence in a series of lines of text to
        be printed exactly as written.
        > you can also use ''' single quote 3 times, not sure what's 
        special about this though


Documentation
===========
* the "pydoc" module creates and provides documentation for modules > ex: bash_shell$ pydoc raw_input



DATA TYPES
===========
    > multiplying a string times a integer, concats string to self that
    many times ex:      "hi" * 3 = "hihihi"
    > Lists
        > like arrays in other languages
        > example:      eyes = [ 'brown', 'blue' , 'green']
        > access list elements with []
            ex: animals[0] = "bear"
    > Tuples
        > immutable lists, possibly distinct data types grouped b/c of some shared property

    > both lists and tuples are square bracket indexed, and can be accesses using slicing
        > list slicing
            [start:stop:step] # you can omit elements, if you want, certain values are defaults
        > start is the first element you want, value at stop is omitted (stop - start) is length of slice
        > step defaults to 1
        > start defaults to 0, and stop defaults to length of the list, string etc.
            ex: [1:]  --> give everything from index 1 and up
            ex: [1::2] --> give every other element from index 1 and up
            ex: [1:-1] --> everything but the first and last element
            ex: [:-1] --> everything but the last element
            ex: [:] --> gives entire list

            ex: [::-1] --> reverses a string, default start (at 0), default stop(at length of string), but 
                go backwards
    > dictionaries:
        > like hash maps
        > syntax:       { key:value, key:value, ...}
        > have a constructor to define via an iterable too
            works like this:
                d = {}
                for x, y in iterable:
                    d[x] = y
            > example: dict( [ (x, j) for x, j in enumerate(iterable)] )
        > return all entries as (key, value) tuples:
            > use dict.items()
    > set
        > similar to a list, but works like a mathematical set
        > there is no ordering, indexing and slicing aren't allowed, sequence-like behavior not allowed
            > operations
                > x <= y    # is subset, is x a subset of y
                > x >= y    # is superset, is x a superset of y
                > x | y     # union of sets x and y
                > x & y     # new set, the intersection of x and y (common elements only)
                > x - y     # new set, set difference ; elements of x that aren't in y
                > x ^ y     # symmetric difference, elements that are only in x or only in y
        > can declare a set from a generator expression
            ex: new_set = set( x for x in some_list)
    > frozenset
        > like a set but it's immutable ( no add or remove)


Platform specifics
===========
* type pydoc os to learn about OS specific information python can
    provide
* pydoc sys to obtain command line arguments, access to the path environment variable and more



File I/O
===========
* use the open(filename) function call,
* default is reading mode
use open(filename, 'w') for writing mode
    NOTE: writing mode will truncate() (i.e. delete) old file
    contents
* READING MODE
	+ read() -- returns the entire input file as a string 
	+ readlines() -- returns a list of strings, each string is a line in the file
* see pydoc open() for more options
* see pydoc file	for info on file objects
* use seek(index) to change read/write position



Importing into Python interpreter
===========
* type:         python_prompt>> import <filename_to_import>
* type filename without file-extension
* to use a function defined  in the file, type:
    filename_imported.function_desired()
* when imported your file is considered a separate module
* use help(filename) to get help for the entire module
* use help(filename.function) to get help for a single function

* type from <filename> import * 
    > to import everything & not have to specify filename before
    function calls


logic expressions
====================
* use "and" "or" "not" instead of "&&", "||" , "!" like in c++ or java
* caret "^" denotes bitwise xor



Conditional Statements
===========

if condition :
    # code
elif condition :
    # code
    ...
else :
    # code

* if <variable_name> :
    # evaluates to true if the variable is not None, or not empty
    # i.e. if it's a string it's not "", if it's a list it's not []
    # experiment with this

* neat conditional statements
    > if x is in container: # where container is a list, tuple, set etc...
    > if x is y :  # returns true if x is identical to y, i.e. they point to
        the same object. This is not the same as ==
        ex: if x is None
* conditional statement inside assignment:
    > I believe newer python versions have a ternary statement like c++/java
    >  example: x = ( 1 if x%2 == 0 else 0)
        # parentheses are not necessary, but I like to use them 



Loops
===========

for i in <list_type>
    # code on each list element
    # works even for mixed lists

    # use enumerate(iterator) to iterate and have an index value too

for i in range(x,y)
    # code to traverse the elements

while condition:
    # code

    Example :
            while i < 6 :
                print "hi"


* a for loop actually breaks down into this

    it = iter(items)
    try:
        while True:
            x = next(it)
            # loop body below
            print x
        except StopIteration:
            pass


defining functions
====================
* use the def keyword
* syntax:
    def function_name():
        # code
* can define a function inside another function, the outer function's
    variables are within the inner function's scope
    ex:

    def fib(n):
        def fib_rec(v1, v2, count):
            if n >= stop:
                return v2
            else:
                return fib_rec(v2, v1+v2, count + 1)
        return fib_rec(0, 1, 1)

        # note that fib_rec can "see" the variable n


STRINGS
===========
    > remember strings are internally just a list of characters
    > Joining Two Strings
        "joining_str".join([array_of_strings_to_join])
        ex: "*".join(['1', '2', '3'])   --> "1*2*3"
        ex: ",".join(['1', '2', '3'])   --> "1,2,3"
    > splitting strings:
        "some_string".split()       # splits on space by default
    > string translation tables
        # useful to change certain characters in a string to
        # other characters
        table = string.maketrans('original_chars', 'new_chars')
        some_str.translate(table) ---> translated_str


Assignment Peculiarities
====================
* can assign the parts of a tuple,  string, or list in one assignment
    ex: a, b, c = (1, 2, 3)     # results in a == 1, b == 2, c == 3
    ex: a, b, c = "xyz"         # results in a == 'x', b == 'y' etc...
* can have multiple assignments on one line:
    example:    x, y = 1 , 2
* underscore is often used as a throwaway variable
    > example:  _, y = ['mon', 'tues']      # we only care about 'tues' and we assign 'mon' to _ to get to what we want
* in interactive mode, underscore is the value of the previous calculation


List comprehensions
====================
* quickly and concisely create a list
* general use is for making a new list from an existing sequence
    by applying an operation to each member of original 
    sequence, or to extract a subsequence that satisfies
    certain conditions

    ex: [ name.upper() for name in udacity_tas]
    ex: [ x**y for x, y in base_exp_tuples ]
    ex: [ x**2 for x in range(10) ]


* can weed out entries in the comprehension using if
    statements

    ex: [ name + country for name, country, course in ta_data
            if country != 'USA']

* syntax 
    [ expression for_clause optional_for_or_if_clauses]

    > for and if statements must be ordered the same way
    they'd be if written in a structure of nested loops 



Generator Expressions
====================
* Generator expression syntax:
    ( term for-clause optional_for_if_clauses )

    > like a list comprehension "[]" means list, "()" means
        generator expression
* a generator expression is like a "promise". It's not evaluated
    right away, but only as its elements are needed (Lazy evaluation).
* next( generator_expression ) ---> next value returned
    > unless there's no values left, then StopIteration exception is returned
* usually use generators inside a for-loop, or convert to list, so
    StopException isn't encountered


Star Args
====================
def something (fn, *args)
    // means this function takes up any number of arguments,
    // they should all be joined in a tuple called args
* star is also used to unpack the variable number of arguments
to a function. When a function has variable arguments,
they are received as a tuple


Generator Functions
====================
* Example:

    def ints(start, end):
        i = start
        while i <= end:
            yield i
            i = i + 1

    As soon as yield statement is encountered, we return, but 
    we remember where function left off

    L = ints(0, 1000) # L is a generator
    # can use L in a for loop or access elements separately

    # allows for infinite sequences if we modify the ints function so
        while-loop condition is " i <= end or end is None "


Profiling
====================
    > $ python -m cProfile <file_to_profile.py>
    > gives a nice table w/ profile data

    > inside python:
        import cProfile
        cProfile.run('test()')



Decorator functions
====================
* A decorator is a function that wraps another
    function (for memoization, call tracing, or other purposes)
* REMEMBER Norvig's discussion about the composability of functions
* a decorator is defined like an ordinary function, but of course it
    returns the decorated function
* to "decorate" an existing function simply put "@decorator_functon" over
the definition of the function to decorate
* use update_wrapper() from the functools library to update function
names when using a decorator

* see cs212/unit3 for examples



Useful functions/libraries
====================
* map(function, iterable)
    # apply the function to each element in the iterable


    # multiple iterables can be passed, but the function must
    # accept the same number of arguments as iterables given
    # iterables are processed in parallel

* enumerate(iterable, start=0)
    > returns list of (index, element) tuples
* zip(iterable1, iterable2, ...)
    > returns a list of tuples, where the ith tuple contains the ith element from each iterable provided
    > truncated to length of shortest tuple
    zip() in conjunction with * can be used to unzip a list
        ex: zipped = zip( [1, 2, 3], [4, 5, 6] ) # zips two lists
                    ---> [(1,4), (2, 5), (3,6) ] # this is the value of zipped
        ex: x, y = zip(*zipped) # unzipping the two lists, we unpack the elements of zipped
            result x == (1, 2, 3)  and y == (4, 5, 6)

    > neat trick to transpose a matrix ( represented as a list of lists):
        map(list, zip(*matrix))
* sorted( iterable )
    # also .sort() for lists
* range(start, stop, step)
    > produce an iterable range??, used often in loops
* itertools
    > useful for permutations/combinations 
    > offers a variety of iteration facilities
    > LOOK @ when you have time!!!!
* re
    > regular expressions library
* random library
    > for random number generation
    > call random.seed() to seed with system time by default 
    > use random.randint(start, stop) # to get an integer in the range desired
    > use random.choice(iterable)
            to choose randomly from a set of options



Testing Code
====================
assert condition    # works like the C assert macro

* usually used like:
    assert function(input) == expected_output



Exceptions
====================
*    try:
        # some code
     except SomeError:
        # exception handling code

    example:
        try:
            y = x/ 0
        except ArithmeticError:
            return False
* to raise an exception:
    example:    raise ValueError


Helpful Functions
====================
* id(PythonObject) -- returns a unique long that is the identity of the python object
* override an object's __str__() function to have functionality like Java's toString() method
