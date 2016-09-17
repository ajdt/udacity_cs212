def csuccessors(state):
    M1, C1, B1, M2, C2, B2 = state
    if B1 > 0:
        items += [(sub(state, delta) a +'->')
                for delta,a in deltas.items()]
    if B2 > 0:
        items += [(add(state, delta), '<-' + a)
                for delta, a in deltas.items() ]
    return dict(items)

deltas = {(2, 0, 1, -2, 0, -1):'MM'
        (0, 2, 1, 0, -2, -1):'CC',
        (1, 1, 1, -1, -1, -1):'MC',
        (1, 0, 1,  -1, 0, -1):'M'
        (0, 1, 1,  0, -1, -1):'C'}

def add(X,Y):
    "add two vectors, X and Y."

    # how is this a generator expression???
    return tuple(x+y for x,y in zip(X,Y))

def sub(X, Y):
    "Subtract Vector Y from X."
    return tuple(x-y for x, y in zip(X,Y))
