# -----------------
# User Instructions
#
# Write a function, subway, that takes lines as input (read more about
# the **lines notation in the instructor comments box below) and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... }
#
# For example, when calling subway(boston), one of the entries in the
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}.
# This means that foresthills only has one neighbor ('backbay') and
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# Once you've defined your subway function, you can define a ride and
# longest_ride function. ride(here, there, system) takes as input
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given
# subway system.

# -------------
# Grading Notes
#
# The subway() function will not be tested directly, only ride() and
# longest_ride() will be explicitly tested. If your code passes the
# assert statements in test_ride(), it should be marked correct.

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


def subway(**lines):
    """Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}"""
    for color, stations in lines.items():
        lines[color] = stations.strip().split(' ')
    subway_map = dict([(s, {}) for stations in lines.values() for s in stations ])

    for color, station_list in lines.items():
        for index, station in enumerate(station_list):
            if index == (len(station_list) - 1) :
                continue
            station_map, neighbor = subway_map[station], station_list[index+1]
            neighbor_map = subway_map[neighbor]
            station_map[neighbor] = color
            neighbor_map[station] = color
    return subway_map

boston = subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')

#@trace
def ride(here, there, system=boston):
    "Return a path on the subway system from here to there."
    def successors(state):
        #print "state is ", state
        return system[state]

    return shortest_path_search(here, successors, lambda state: state == there )

@trace
def longest_ride(system):
    """"Return the longest possible 'shortest path'
    ride between any two stops in the system."""
    return max( [ ride(h,t,system) for h in system.keys() for t in system.keys() if h != t], key=len)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def test_ride():
    assert ride('mit', 'government') == [
        'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    assert ride('mattapan', 'foresthills') == [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
    assert ride('newton', 'alewife') == [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
    assert (path_states(longest_ride(boston)) == [
        'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
        'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or
        path_states(longest_ride(boston)) == [
                'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles',
                'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
    assert len(path_states(longest_ride(boston))) == 16
    return 'test_ride passes'

print test_ride()

# Norvig's solution is almost identical to mine
# except lambda's are used instead of defining goal
# and successor functions
#
# also the collections module is used to initialize
# the dictionary for every station to a default
# dictionary

# ex: successors = collections.defaultdict(dict)

# find out more about the collections module
