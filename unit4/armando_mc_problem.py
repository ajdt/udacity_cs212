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

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    succ = {}
    if M1 < C1 or M2 < C2 :
        return succ
    if B1 > 0 : # there are boats on side 1
        if M1 > 1:
            succ[(M1 - 2, C1, B1-1, M2+2, C2, B2+1)] = 'MM->'
        if M1 > 0 and C1 > 0 :
            succ[(M1-1, C1 - 1, B1-1, M2+1, C2+1, B2+1)] = 'MC->'
        if M1 > 0 :
            succ[(M1-1, C1, B1-1, M2+1, C2, B2+1)] = 'M->'
        if C1 > 0 :
            succ[(M1, C1-1, B1-1, M2, C2+1, B2+1)] = 'C->'
        if C1 > 1 :
            succ[(M1, C1-2, B1-1, M2, C2+2, B2+1)] = 'CC->'
    if B2 > 0 : # there's a boat on side two
        if M2 > 1:
            succ[(M1+2, C1, B1+1, M2-2, C2, B2-1)] = '<-MM'
        if M2 > 0 and C2 > 0 :
            succ[(M1+1, C1+1, B1+1, M2-1, C2-1, B2-1)] = '<-MC'
        if M2 > 0 :
            succ[(M1+1, C1, B1+1, M2-1, C2, B2-1)] = '<-M'
        if C2 > 0 :
            succ[(M1, C1+1, B1+1, M2, C2-1, B2-1)] = '<-C'
        if C2 > 1 :
            succ[(M1, C1+2, B1+1, M2, C2-2, B2-1)] = '<-CC'
    return succ

def mc_solver(start=(3, 3, 1, 0, 0, 0), goal=None):
    """Solve the missionaries and cannibals problem.
    State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start(1) and other (2) sides.
    Find a path that goes form the initial state to the goal state (which, if
    not specified, is the state with no people or boats on the start side.)"""
    if goal is None:
        goal = (0, 0, 0, start[0]+start[3], start[1]+start[4], start[2]+start[5])

    frontier, explored = [ [start] ], set([ start ])
    print goal

    while frontier:
        path = frontier.pop(0)
        last_state = path[-1]
        if last_state == goal:
            return path
        for new_state, action in csuccessors(last_state).items():
            if new_state not in explored:
                explored.add(new_state)
                frontier.append(path + [action, new_state])
        if csuccessors(last_state) == {}:
            print "dead end: ", path
        frontier.sort(key=len)
    return None

print "solution: ", mc_solver((3,3,3,0,0,0))

