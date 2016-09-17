import doctest

class Test: """

# denote a test case with ">>>"
expected output is right below
>>> successors(0, 0, 4, 9)
{(0, 9): 'fill Y', (0, 0), 'empty Y', (4, 0): 'fill X'}

>>> successors(3, 5, 4, 9)
{(4,5): 'fill X', (4, 4):'X<-Y', (3, 0):'empty Y', (3,9): 'fill Y', (0, 5):'empty X'...}

# can also define functions for more extensive testing

def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X, Y, goal))

"""

# to run the test just type:
print doctest.testmod()
# tests the current module by default, pass module name
# as argument to test different module
