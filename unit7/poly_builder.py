


def poly_build_str(coefficients):
    " a function that builds a coefficient string from a coefficient tuple"
    str = ""
    for (exp, coeff) in enumerate(coefficients):
        if coeff == 0 :
            continue
        constant = "" if coeff == 1 else "%d" % coeff
        var = "" if exp == 0 else  ("x" if exp == 1 else "x**%d" % exp)
        if not constant and not var: # both parts are equal to 1
            term = "1"
        elif not constant or not var: # only one part is equal to 1
            term = constant + var
        else :
            term = constant + "*" + var

        # append the current term to string
        str = term + str if not str else term + " + " + str
    return str


print poly_build_str( (1, 2, 3, 4, 5) )
assert poly_build_str( (1, 2, 3, 4, 5) ) == "5*x**4 + 4*x**3 + 3*x**2 + 2*x + 1"
assert poly_build_str( (1, 0, 3, 0, 5) ) == "5*x**4 + 3*x**2 + 1"

