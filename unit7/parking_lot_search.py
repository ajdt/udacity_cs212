"""
UNIT 4: Search

Your task is to maneuver a car in a crowded parking lot. This is a kind of
puzzle, which can be represented with a diagram like this:

| | | | | | | |
| G G . . . Y |
| P . . B . Y |
| P * * B . Y @
| P . . B . . |
| O . . . A A |
| O . S S S . |
| | | | | | | |

A '|' represents a wall around the parking lot, a '.' represents an empty square,
and a letter or asterisk represents a car.  '@' marks a goal square.
Note that there are long (3 spot) and short (2 spot) cars.
Your task is to get the car that is represented by '**' out of the parking lot
(on to a goal square).  Cars can move only in the direction they are pointing.
In this diagram, the cars GG, AA, SSS, and ** are pointed right-left,
so they can move any number of squares right or left, as long as they don't
bump into another car or wall.  In this diagram, GG could move 1, 2, or 3 spots
to the right; AA could move 1, 2, or 3 spots to the left, and ** cannot move
at all. In the up-down direction, BBB can move one up or down, YYY can move
one down, and PPP and OO cannot move.

You should solve this puzzle (and ones like it) using search.  You will be
given an initial state like this diagram and a goal location for the ** car;
in this puzzle the goal is the '.' empty spot in the wall on the right side.
You should return a path -- an alternation of states and actions -- that leads
to a state where the car overlaps the goal.

An action is a move by one car in one direction (by any number of spaces).
For example, here is a successor state where the AA car moves 3 to the left:

| | | | | | | |
| G G . . . Y |
| P . . B . Y |
| P * * B . Y @
| P . . B . . |
| O A A . . . |
| O . . . . . |
| | | | | | | |

And then after BBB moves 2 down and YYY moves 3 down, we can solve the puzzle
by moving ** 4 spaces to the right:

| | | | | | | |
| G G . . . . |
| P . . . . . |
| P . . . . * *
| P . . B . Y |
| O A A B . Y |
| O . . B . Y |
| | | | | | | |

You will write the function

    solve_parking_puzzle(start, N=N)

where 'start' is the initial state of the puzzle and 'N' is the length of a side
of the square that encloses the pieces (including the walls, so N=8 here).

We will represent the grid with integer indexes. Here we see the
non-wall index numbers (with the goal at index 31):

 |  |  |  |  |  |  |  |
 |  9 10 11 12 13 14  |
 | 17 18 19 20 21 22  |
 | 25 26 27 28 29 30 31
 | 33 34 35 36 37 38  |
 | 41 42 43 44 45 46  |
 | 49 50 51 52 53 54  |
 |  |  |  |  |  |  |  |

The wall in the upper left has index 0 and the one in the lower right has 63.
We represent a state of the problem with one big tuple of (object, locations)
pairs, where each pair is a tuple and the locations are a tuple.  Here is the
initial state for the problem above in this format:
"""

puzzle1 = (
 ('@', (31,)),
 ('*', (26, 27)),
 ('G', (9, 10)),
 ('Y', (14, 22, 30)),
 ('P', (17, 25, 33)),
 ('O', (41, 49)),
 ('B', (20, 28, 36)),
 ('A', (45, 46)),
 ('|', (0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 32, 39,
        40, 47, 48, 55, 56, 57, 58, 59, 60, 61, 62, 63)))

# A solution to this puzzle is as follows:

#     path = solve_parking_puzzle(puzzle1, N=8)
#     path_actions(path) == [('A', -3), ('B', 16), ('Y', 24), ('*', 4)]

# That is, move car 'A' 3 spaces left, then 'B' 2 down, then 'Y' 3 down,
# and finally '*' moves 4 spaces right to the goal.

# Your task is to define solve_parking_puzzle:

N = 8

def solve_parking_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""

    goal_location = get_goal_location(N)
    goal, walls, cars = None, None, []
    for x in start :
        if x[0] == '|':
            walls = x
        elif x[0] == '@':
            goal = x
        else:
            cars.append(x)
    start = (goal,) + tuple(cars) + (walls,)
    def is_goal(state):
        board = make_board(state, N)
        return board[goal_location] == '*'
    return shortest_path_search(start, successors, is_goal, N)
# But it would also be nice to have a simpler format to describe puzzles,
# and a way to visualize states.
# You will do that by defining the following two functions:

def locs(start, n, incr=1):
    "Return a tuple of n locations, starting at start and incrementing by incr. If n is negative, returns empty tuple "
    if n <= 0:
        return tuple()
    return tuple( start + i*incr for i in range(n) )


def get_goal_location(N):
    " gives the goal location for an NxN grid. Goal is placed in middle of right border."
    # N-1 is top-most right position, and we add N to that (n/2 -1 )times
    return (N-1)+(N-1)/2 *N

def grid(cars, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to
    indicate there are walls all around the NxN grid, except at the goal
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this. The variable 'cars'  is a
    tuple of pairs like ('*', (26, 27)). The return result is a big tuple
    of the 'cars' pairs along with the walls and goal pairs."""
    # for wall locations, the order is top border, bottom, left
    wall_locations = locs(0, N)+locs(N*(N-1), N) + locs(N,N-2, N)
    right_side = list(locs(N-1+N, N-2, N))
    goal_loc = get_goal_location(N)
    right_side.remove(goal_loc) # remove goal, location from the list of wall_locations
    wall_locations = wall_locations + tuple(right_side)

    # order of the state tuple is goal_location, cars, wall_locations
    return ( ('@', (goal_loc,)), ) + cars + (('|', wall_locations), )


def make_board(state, N=N):
    " using a state tuple, create a full representation of a board"
    grid = ['.']*(N*N) # initialize board
    for (symbol, locations) in state: # fill board according to squares
        for loc in locations:
            grid[loc] = symbol
    return grid

def car_delta(car):
    " returns the delta for car movement. car is a tuple (symbol, (position_tuple)). Assumes each car takes up @ least 2 squares."
    return abs( car[1][0] - car[1][1]) # subtracts two position values from each other, assumed tuple is ordered


# this function assumes the position tuple for a car is in ascending order
def movement_range(car, delta, board):
    """ returns a tuple of the range a car can move of the form (pos, neg) where pos is the movement range
    in the positive direction (DOWN or RIGHT) and neg is movement in the negative direction (UP or LEFT)"""
    return ( num_moves(board, car[1][-1], abs(delta)), -1*num_moves(board, car[1][0], -abs(delta)) )

def num_moves(board, start, delta):
    " returns the number of moves a car can make from the start position with delta"
    squares, start = 0, start + delta
    while board[start] == '.' or board[start] == '@':
        squares += 1
        start += delta
    return squares

def shift_car(car, n, delta):
    return ( (car[0], tuple(map(lambda x: x + n*delta, car[1]))), )

def successors(state, N=N):
    board = make_board(state, N)
    cars = state[1:-1]
    state_action_pairs = []
    for (idx, c) in enumerate(cars):
        delta = car_delta(c)
        pos, neg = movement_range(c, delta, board)
        if pos != 0 :
            for i in range(1, pos+1):
                new_state = (state[0],) + cars[0:idx] + (shift_car(c, i, delta)) + cars[idx+1:] + state[-1:]
                action = (c[0], i*delta)
                state_action_pairs.append( (new_state, action) )
        if neg != 0 :
            for i in range(-1, neg-1, -1):
                new_state = (state[0],) + cars[0:idx] + (shift_car(c, i, delta)) + cars[idx+1:] + state[-1:]
                action = (c[0], i*delta)
                state_action_pairs.append( (new_state, action) )
    return dict(state_action_pairs)




def show(state, N=N):
    "Print a representation of a state as an NxN grid."
    board = make_board(state, N)
    # Now print it out
    for i,s in enumerate(board):
        print s,
        if i % N == N - 1: print

# Here we see the grid and locs functions in use:

puzzle1 = grid((
    ('*', locs(26, 2)),
    ('G', locs(9, 2)),
    ('Y', locs(14, 3, N)),
    ('P', locs(17, 3, N)),
    ('O', locs(41, 2, N)),
    ('B', locs(20, 3, N)),
    ('A', locs(45, 2))))

puzzle2 = grid((
    ('*', locs(26, 2)),
    ('B', locs(20, 3, N)),
    ('P', locs(33, 3)),
    ('O', locs(41, 2, N)),
    ('Y', locs(51, 3))))

puzzle3 = grid((
    ('*', locs(25, 2)),
    ('B', locs(19, 3, N)),
    ('P', locs(36, 3)),
    ('O', locs(45, 2, N)),
    ('Y', locs(49, 3))))


# Here are the shortest_path_search and path_actions functions from the unit.
# You may use these if you want, but you don't have to.

def shortest_path_search(start, successors, is_goal, N):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in sorted(successors(s, N).items(), key=lambda x : abs(x[1][1])):
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

show(puzzle1)

def test():
    # test movement_range() function
    assert set( (car[0], movement_range(car, car_delta(car), make_board(puzzle1))) for car in puzzle1[1:-1] ) == set([
            ('*', (0, 0)),
            ('G', (3, 0)),
            ('Y', (1, 0)),
            ('P', (0, 0)),
            ('O', (0, 0)),
            ('B', (2, -1)),
            ('A', (0, -3)) ])
    assert set( (car[0], movement_range(car, car_delta(car), make_board(puzzle2))) for car in puzzle2[1:-1] ) == set([
        ('*', (0, -1)) ,
        ('B', (1, -1)) ,
        ('P', (0, 0)) ,
        ('O', (0, 0)) ,
        ('Y', (1, -1))  ])

    # testing shift_car() function
    car , n, delta= ('A', (1, 2, 3, 4)), 2, 8
    assert shift_car(car, n, delta) == (('A', (17, 18, 19, 20)), )
    assert shift_car(car, 1, delta) == (('A', (9, 10, 11, 12)),)
    assert shift_car(car, -2, 4) == (('A', (-7, -6, -5, -4)),)

    # testing successors function
    assert sorted(successors(puzzle1).values()) == [('A', -3), ('A', -2), ('A', -1), ('B', -1), ('B', 1), ('B', 2), ('G', 1), ('G', 2), ('G', 3), ('Y', 1)]
    assert sorted(successors(puzzle2).values()) == sorted( [ ('B', -1), ('B', 1), ('Y', 1), ('Y', -1), ('*', -1) ] )


    # regression tests for solve_parking_puzzle
    #   these are the solutions obtained by my first version of the solver
    #print solve_parking_puzzle(puzzle1)[1::2]
    solution = solve_parking_puzzle(puzzle1)
    print "start state"
    for state in solution[0::2] :
       show(state)
       print
    print solution[1::2]
    assert solve_parking_puzzle(puzzle1)[1::2] == [('A', -3), ('Y', 24), ('B', 16), ('*', 4)]
    #assert solve_parking_puzzle(puzzle2)[1::2] == [('B', -1), ('P', 3), ('O', -3), ('P', -3), ('Y', -2), ('B', 3), ('*', 4)]
    #assert solve_parking_puzzle(puzzle3)[1::2] == [('B', -1), ('P', -3), ('O', -4), ('Y', 3), ('P', 3), ('B', 3), ('*', 5)]
    #assert len(solve_parking_puzzle(puzzle1)[1::2]) == 4
    #assert len(solve_parking_puzzle(puzzle2)[1::2]) == 7
    #assert len(solve_parking_puzzle(puzzle3)[1::2]) == 7

    sz = 9
    puzzle4 = grid((
        ('*', locs(38, 2)),
        ), sz)
    assert solve_parking_puzzle(puzzle4, sz)[1::2] == [('*', 5)]
    puzzle5 = grid((
        ('*', locs(38, 2)),
        ('A', locs(22, 3, sz)),
        ('B', locs(49, 3)),
        ('O', locs(58, 2)),
        ('X', locs(24, 3, sz)),
        ('C', locs(46, 2)),
        ('Z', locs(10, 3)),
        ('Y', locs(14, 3))), sz)
    print
    show(puzzle5, sz)
    print solve_parking_puzzle(puzzle5, sz)[1::2]

    size = 6
    puzzle6 = grid((
        ('*', locs(14, 2)),
        ('S', locs(20, 3)),
        ('B', locs(27, 2)),
        ('A', locs(10, 2, size))), size)
    print
    show(puzzle6, size)
    print solve_parking_puzzle(puzzle6, size)[1::2]
    print solve_parking_puzzle(puzzle6, size)[-1]

    print "all tests pass"

from itertools import cycle
cars = cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
hcar = lambda start, l=2: (next(cars), locs(start, l))
vcar = lambda start, l=2: (next(cars), locs(start, l, N))
star = lambda start: ('*', locs(start, 2))

sp = grid((
    hcar( 9, 3), vcar(12, 2), vcar(13, 3), vcar(17, 2), hcar(18, 2),
    star(27),
    hcar(33, 2), vcar(35, 2), vcar(38, 2), vcar(42, 2), hcar(44, 2), hcar(51, 2), hcar(53, 2),
    ))

def hard_tests():
	show(sp)
	print solve_parking_puzzle(sp)[1::2]
#print
#show(puzzle2)
#print
#show(puzzle3)
test()
#hard_tests()
