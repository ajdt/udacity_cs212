"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming.
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""


import itertools
days = mon, tues, wed, thurs, fri = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(days))

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed

    order = next( [(Hamming, 'Hamming'), (Knuth, 'Knuth'), (Minsky, 'Minsky'), (Simon, 'Simon'), (Wilkes, 'Wilkes') ]
                for laptop, droid, tablet, iphone, _ in orderings
                if laptop == wed
                if fri != tablet
                if tablet == tues or iphone == tues
                for programmer, writer, manager, designer, _ in orderings
                if thurs != designer
                if designer != droid
                for Wilkes, Hamming, Minsky, Knuth, Simon in orderings

                if programmer != Wilkes
                if Minsky != writer
                # 3. Of the programmer and the person who bought the droid,
                # one is Wilkes and the other is Hamming.
                if (programmer == Wilkes and droid == Hamming) or (programmer == Hamming and droid == Wilkes)

                # 5. Neither Knuth nor the person who bought the tablet is the manager.
                if Knuth != manager and tablet != manager

                #6. Knuth arrived the day after Simon.
                if Knuth == Simon + 1
                # 10. Knuth arrived the day after the manager.
                if Knuth == manager + 1
                # 11. Of the person who bought the laptop and Wilkes,
                #    one arrived on Monday and the other is the writer.
                if laptop != Wilkes and (laptop == mon and writer == Wilkes) or (laptop == writer and Wilkes == mon)
            )

    order.sort()
    return map(lambda tup: tup[1], order) # return only the names

    # see what's available to us first

print logic_puzzle()


