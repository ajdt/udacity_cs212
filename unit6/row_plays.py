class anchor(set):
    """An anchor is where a new word can be placed;
    has a set of allowable letters."""

LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ANY = anchor(LETTERS) # the anchor that can be any letter

# |A.....BE.C...D.|
mnx, moab = anchor('MNX'), anchor('MOAB')
a_row = [ '|', 'A', mnx, moab, '.', '.',
        ANY, 'B', 'E', ANY, 'C', ANY, '.', ANY,
        'D', ANY, '|']
a_hand = 'ABCEHKN'

def row_plays(hand, row):
    "Returns a set of legal plays in row. A row play is a (start, 'Word') pair"
    results = set()
    ## to each allowable prefix, add all suffixes, keep words
    for (i, sq) in enumerate(row[1:-1], 1):
        if isinstance(sq, anchor):
            pre, maxsize = legal_prefix(i, row)
            if pre : ## Add to the letters already on the board
                start = i - len(pre)
                add_suffixes(hand, pre, start, row, results, anchored=False)
            else: ## Empty to left: go through the set of all possible prefixes
                for pre in find_prefixes(hand):
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(remvoed(hand, pre),
                                pre, start, row, results, anchored=False)


    return results

def legal_prefix(i, row):
    """A legal prefix of an anchor at row[i] is either a
    string of letters already on the board, or new
    letters that fit into an empty space. Return the
    tuple (prefix_on_board, maxsize) to indicate this.
    prefix_on_board is '' when there is empty space on the
    board."""
    s = i
    while is_letter(row[s-1]): s -= 1
    if s < i :
        return (''.join(row[s:i]), i-s)

    while is_empty(row[s-1]) and not isinstance(row[s-1], anchor): s -= 1
    return ('', i-s)

def is_letter(sq):
    "Is this an empty square (no letters, but a valid position on board)"
    return sq == '.' or sq == '*' or isinstance(sq, anchor)

def is_letter(sq):
    return isinstance(sq, str) and sq in LETTERS

def add_suffixes(hand, pre, start, row, results, anchored=True):
    "Add all possible suffixes, and accumulate (start, word) pairs in result"
    i = start + len(pre) # start of suffix

    if pre in WORDS and anchored and not is_letter(row[i])
        results.add( (start, pre) )
    if pre in PREFIXES :
        square = row[i]
        if is_letter[square] :
            add_suffixes(hand, pre+row[i],
                    start, row, results)
        elif is_empty(square) :
            possibilities = sq if isinstance(sq, anchor) else ANY

            for L in hand:
                if L in possibilities :
                    add_suffixes(hand.replace(L, '', 1), pre+L,
                        start, row, results)

    return results



