#----------------
# User Instructions
#
# The function, matchset, takes a pattern and a text as input
# and returns a set of remainders. For example, if matchset
# were called with the pattern star(lit(a)) and the text
# 'aaab', matchset would return a set with elements
# {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
# or all three of the a's in the text.
#
# Your job is to complete this function by filling in the
# 'dot' and 'oneof' operators to return the correct set of
# remainders.
#
# dot:   matches any character.
# oneof: matches any of the characters in the string it is
#        called with. oneof('abc') will match a or b or c.

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        # call matchset recursively to match a subpart of a
        # pattern, then apply the returned set to subsequent
        # subparts...
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        # ****** MY CODE USED FOR THIS CASE
        return set([text[1:]])
        # norvig thought of case where text = ""
        # Need to consider boundary cases more thoroughly!!!
        # Norvig's code:
        #   return set([text[1:]]) if text else null
    elif 'oneof' == op:
        # ****** MY CODE USED FOR THIS CASE
        # Norvig took better advantage of the way
        # string.startswith() works, another example of
        # knowing your language well. He converts
        # the string x to a tuple first
        # Norvig Code:
        #   return set([text[1:]]) if text.startswith(x) else null
        # He setup the components() function to return
        # x as a tuple to make the above line work.
        # alternative code:
        #   return set([text[1:]])
        #       if any(text.startswith(c) for c in x)
        #       else null
        return set( [ text[1:] for letter in x if text.startswith(letter) ])
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)

null = frozenset()

def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y

def test():
    assert matchset(('lit', 'abc'), 'abcdef')            == set(['def'])
    assert matchset(('seq', ('lit', 'hi '),
                     ('lit', 'there ')),
                   'hi there nice to meet you')          == set(['nice to meet you'])
    assert matchset(('alt', ('lit', 'dog'),
                    ('lit', 'cat')), 'dog and cat')      == set([' and cat'])
    assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
    assert matchset(('oneof', 'a'), 'aabc123')           == set(['abc123'])
    assert matchset(('eol',),'')                         == set([''])
    assert matchset(('eol',),'not end of line')          == frozenset([])
    assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])

    return 'tests pass'

print test()
