# Unit 5: Probability in the game of Darts

"""
In the game of darts, players throw darts at a board to score points.
The circular board has a 'bulls-eye' in the center and 20 slices
called sections, numbered 1 to 20, radiating out from the bulls-eye.
The board is also divided into concentric rings.  The bulls-eye has
two rings: an outer 'single' ring and an inner 'double' ring.  Each
section is divided into 4 rings: starting at the center we have a
thick single ring, a thin triple ring, another thick single ring, and
a thin double ring.  A ring/section combination is called a 'target';
they have names like 'S20', 'D20' and 'T20' for single, double, and
triple 20, respectively; these score 20, 40, and 60 points. The
bulls-eyes are named 'SB' and 'DB', worth 25 and 50 points
respectively. Illustration (png image): http://goo.gl/i7XJ9

There are several variants of darts play; in the game called '501',
each player throws three darts per turn, adding up points until they
total exactly 501. However, the final dart must be in a double ring.

Your first task is to write the function double_out(total), which will
output a list of 1 to 3 darts that add up to total, with the
restriction that the final dart is a double. See test_darts() for
examples. Return None if there is no list that achieves the total.

Often there are several ways to achieve a total.  You must return a
shortest possible list, but you have your choice of which one. For
example, for total=100, you can choose ['T20', 'D20'] or ['DB', 'DB']
but you cannot choose ['T20', 'D10', 'D10'].
"""

def test_darts():
    "Test the double_out function."
    assert double_out(170) == ['T20', 'T20', 'DB']
    assert double_out(171) == None
    assert double_out(100) in (['T20', 'D20'], ['DB', 'DB'])
    print test_darts.__name__, " ran successfully "

"""
My strategy: I decided to choose the result that has the highest valued
target(s) first, e.g. always take T20 on the first dart if we can achieve
a solution that way.  If not, try T19 first, and so on. At first I thought
I would need three passes: first try to solve with one dart, then with two,
then with three.  But I realized that if we include 0 as a possible dart
value, and always try the 0 first, then we get the effect of having three
passes, but we only have to code one pass.  So I creted ordered_points as
a list of all possible scores that a single dart can achieve, with 0 first,
and then descending: [0, 60, 57, ..., 1].  I iterate dart1 and dart2 over
that; then dart3 must be whatever is left over to add up to total.  If
dart3 is a valid element of points, then we have a solution.  But the
solution, is a list of numbers, like [0, 60, 40]; we need to transform that
into a list of target names, like ['T20', 'D20'], we do that by defining name(d)
to get the name of a target that scores d.  When there are several choices,
we must choose a double for the last dart, but for the others I prefer the
easiest targets first: 'S' is easiest, then 'T', then 'D'.
"""

def trace(fn) :
    """ decorator that traces a function fn, displaying data for each function call
    and return from a function call"""
    indent = "    " # space for one indentation
    trace.stack_depth = 0

    def traced_fn(*args):

        # print call data
        signature = "%s(%s)" % (fn.__name__, ", ".join(map(repr, args)))
        #print "%s-->%s" % (indent*trace.stack_depth, signature )
        trace.stack_depth += 1
        result = fn(*args)

        # print the results
        print "%s<--%s == %s" % (indent*trace.stack_depth, signature, result)
        trace.stack_depth -= 1

        return result   # must return the same result as the traced function
    return traced_fn

singles = [(i, 'S%d' % i) for i in range(1, 21)] + [(25, 'SB')]
doubles = [(i*2, 'D%d' % i) for i in range(1, 21)] + [(50, 'DB')]
triples = [(i*3, 'T%d' % i) for i in range(1, 21)]

targets = [x[1] for x in (singles+doubles+triples)]
double_values = [ x[0] for x in doubles]
double_with_value = dict(doubles)
arrow_values = set([0]) | set( sorted( [x[0] for x in (singles+doubles+triples)] ))
missed_board = 'OFF'

# set up a dict of all items with the given values
has_value = dict( [(x, []) for x in arrow_values])
for value, target in (singles + doubles + triples) :
    has_value[value].append(target)
value_of = dict( [ (x, y) for y, x in singles + doubles + triples])

#@trace
def double_out(total, depth=1):
    """Return a shortest possible list of targets that add to total,
    where the length <= 3 and the final element is a double.
    If there is no solution, return None."""
    if depth == 3:
        if total in double_values :
            return [ double_with_value[total]]
        else:
            return None
    else:
        for x in arrow_values:
            res = double_out(total-x, depth + 1)
            if res :
                return ([] if x == 0 else [has_value[x][0] ]) + res
    return None

"""
It is easy enough to say "170 points? Easy! Just hit T20, T20, DB."
But, at least for me, it is much harder to actually execute the plan
and hit each target.  In this second half of the question, we
investigate what happens if the dart-thrower is not 100% accurate.

We will use a wrong (but still useful) model of inaccuracy. A player
has a single number from 0 to 1 that characterizes his/her miss rate.
If miss=0.0, that means the player hits the target every time.
But if miss is, say, 0.1, then the player misses the section s/he
is aiming at 10% of the time, and also (independently) misses the thin
double or triple ring 10% of the time. Where do the misses go?
Here's the model:

First, for ring accuracy.  If you aim for the triple ring, all the
misses go to a single ring (some to the inner one, some to the outer
one, but the model doesn't distinguish between these). If you aim for
the double ring (at the edge of the board), half the misses (e.g. 0.05
if miss=0.1) go to the single ring, and half off the board. (We will
agree to call the off-the-board 'target' by the name 'OFF'.) If you
aim for a thick single ring, it is about 5 times thicker than the thin
rings, so your miss ratio is reduced to 1/5th, and of these, half go to
the double ring and half to the triple.  So with miss=0.1, 0.01 will go
to each of the double and triple ring.  Finally, for the bulls-eyes. If
you aim for the single bull, 1/4 of your misses go to the double bull and
3/4 to the single ring.  If you aim for the double bull, it is tiny, so
your miss rate is tripled; of that, 2/3 goes to the single ring and 1/3
to the single bull ring.

Now, for section accuracy.  Half your miss rate goes one section clockwise
and half one section counter-clockwise from your target. The clockwise
order of sections is:

    20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5

If you aim for the bull (single or double) and miss on rings, then the
section you end up on is equally possible among all 20 sections.  But
independent of that you can also miss on sections; again such a miss
is equally likely to go to any section and should be recorded as being
in the single ring.

You will need to build a model for these probabilities, and define the
function outcome(target, miss), which takes a target (like 'T20') and
a miss ration (like 0.1) and returns a dict of {target: probability}
pairs indicating the possible outcomes.  You will also define
best_target(miss) which, for a given miss ratio, returns the target
with the highest expected score.

If you are very ambitious, you can try to find the optimal strategy for
accuracy-limited darts: given a state defined by your total score
needed and the number of darts remaining in your 3-dart turn, return
the target that minimizes the expected number of total 3-dart turns
(not the number of darts) required to reach the total.  This is harder
than Pig for several reasons: there are many outcomes, so the search space
is large; also, it is always possible to miss a double, and thus there is
no guarantee that the game will end in a finite number of moves.
"""


sections = "20 1 18 4 13 6 10 15 2 17 3 19 7 16 8 11 14 9 12 5".split(' ')
def split_target(target):
    "split target into ring and section"
    return target[0], target[1:]
def get_adjacent_sections(section):
    idx = sections.index(section)
    left = sections[idx-1]
    right = sections[idx+1] if idx+1 < len(sections) else sections[0]
    return left, right

#@trace
def ring_outcome(target, miss):
    ring, section = split_target(target)
    if target == 'SB' :
        return { 'SB': 1.0-miss, 'DB': miss/4.0, 'S': miss*3.0/4.0}
    elif target == 'DB' :
        miss = miss*3.0
        return { 'DB': 1.0-miss, 'SB': miss/3.0, 'S': miss*2.0/3.0}
    elif ring == 'T':
        return { 'T': 1.0 - miss, 'S': miss }
    elif ring == 'D':
        return { 'D': 1.0 - miss, missed_board:miss/2.0, 'S':miss/2.0}
    elif ring == 'S':
        miss = miss/5.0
        return { 'S':1.0-miss, 'D':miss/2.0, 'T':miss/2.0}
    else:
        return {}

#@trace
def section_outcome(target, miss) :
    results = {}
    if target in ['SB', 'DB'] :
        for x in sections:
            results[x] = miss/20.0
        results['B'] = 1.0 - miss
    else :
        ring, section = split_target(target)
        left, right = get_adjacent_sections(section)
        results[section] = 1.0 - miss
        results[left] = miss/2.0
        results[right] = miss/2.0

    return results



#@trace
def outcome(target, miss):
    "Return a probability distribution of [(target, probability)] pairs."
    results = {}
    s_outcome = section_outcome(target, miss)
    r_outcome= ring_outcome(target, miss)
    for (ring, p) in r_outcome.items():
        if ring == missed_board:
            continue
        for ( sect, q) in s_outcome.items():
            if ring in ['SB', 'DB']:
                if sect != 'B': # hit the bull on ring, but missed on section
                    for x in sections:
                        update_entry(results, 'S'+x, p*q/20.0, 1)
                else:
                    update_entry(results, ring, p*q, 2) # ring actually describes target completely
            else :
                if sect == 'B': # hit bull on section, missed on ring
                    for x in sections:
                        update_entry(results, 'S'+x, p*q/20.0, 3)
                else :
                    update_entry(results, ring+sect, p*q, 4)
    return results

def update_entry(results, key, value, x, default=0):
    " add to the value in dictionary if it exits"
    temp = results.get(key, default)
    results[key] = temp + value



def best_target(miss):
    "Return the target that maximizes the expected score."
    #your code here
    scores = [ (expected_score(x, miss), x) for x in targets ]
    scores.sort(reverse=True)
    return scores[0][1] # we return the target with maximal expected score


def expected_score(target, miss) :
    " gives the expected score for a single target"
    total = 0
    for ( target, probability) in outcome(target, miss).items() :
        total += value_of[target]*probability
    return total


def same_outcome(dict1, dict2):
    "Two states are the same if all corresponding sets of locs are the same."
    return all(abs(dict1.get(key, 0) - dict2.get(key, 0)) <= 0.0001
               for key in set(dict1) | set(dict2))

def test_darts2():
    assert best_target(0.0) == 'T20'
    assert best_target(0.1) == 'T20'
    assert best_target(0.4) == 'T19'
    assert same_outcome(outcome('T20', 0.0), {'T20': 1.0})

    assert same_outcome(outcome('T20', 0.1),
                        {'T20': 0.81, 'S1': 0.005, 'T5': 0.045,
                         'S5': 0.005, 'T1': 0.045, 'S20': 0.09})
    print "*"*30
    #compare_dicts({'S9': 0.016, 'S8': 0.016, 'S3': 0.016, 'S2': 0.016, 'S1': 0.016,
    #         'DB': 0.04, 'S6': 0.016, 'S5': 0.016, 'S4': 0.016, 'S20': 0.016,
    #         'S19': 0.016, 'S18': 0.016, 'S13': 0.016, 'S12': 0.016, 'S11': 0.016,
    #         'S10': 0.016, 'S17': 0.016, 'S16': 0.016, 'S15': 0.016, 'S14': 0.016,
    #         'S7': 0.016, 'SB': 0.64}, outcome('SB', 0.2))
    assert (same_outcome(
            outcome('SB', 0.2),
            {'S9': 0.016, 'S8': 0.016, 'S3': 0.016, 'S2': 0.016, 'S1': 0.016,
             'DB': 0.04, 'S6': 0.016, 'S5': 0.016, 'S4': 0.016, 'S20': 0.016,
             'S19': 0.016, 'S18': 0.016, 'S13': 0.016, 'S12': 0.016, 'S11': 0.016,
             'S10': 0.016, 'S17': 0.016, 'S16': 0.016, 'S15': 0.016, 'S14': 0.016,
             'S7': 0.016, 'SB': 0.64}))
    print "all tests pass"

def print_dict(dictionary):
    print "{",
    for (k, v) in dictionary.items():
        print k, ":", v, ", ",
    print "}"
def compare_dicts(d1, d2):
    for (k, v) in d1.items():
        print k, ":", v, "\t", d2.get(k,0)


#test_darts()
test_darts2()
