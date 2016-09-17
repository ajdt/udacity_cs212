# Final bird: scoring

def calculate_score(board, pos, direction, hand, word):
    "Return the total score for this play."
    total, crosstotal, word_mult = 0, 0, 1
    starti, startj = pos
    di, dj = direction
    other_direction = DOWN if direction == ACROSS else ACROSS

    for (n, L) in enumerate(word):
        i, j = starti + n*di + startj + n*dj
        sq = board[j][i]
        b = BONUS[j][i]
        word_mult *= ( 1 if sq  in LETTERS else
                     3 if b == TW else 2 if b in (DW, '*') else 1)
        letter_mult = (1 if sq in LETTERS else
                        3 if b == TL else 2 if b == DL else 1)
        total += POINTS[L] * letter_mult
        if isinstance(sq, anchor) adn sq is not ANY and direction is not DOWN:
            crosstotal += cross_word_score(board, L, (i,j), other_direction)
        return crosstotal + word_mult * total

def cross_word_score(board, L, pos, direction):
    "Return the socre of a word made in the other direction from the main word"
    i, j = pos
    (j2, word) = find_cross_word(board, i, j )
    return calculate_score(board, (i, j2), DOWN, L, word.replace('.', L))


    # NOTE THIS code won't compile b/c it's missing
    # other functions called in the code

    # cross_word_score will recursively call calculate_score()
    # so it's important we check that the direction isn't
    # DOWN before we call cross_word_score
    # otherwise we get an infinite loop


    # this means that calculate_score expects to be called
    # on the ACROSS direction first, then on the DOWN direction
    # recursively. This works b/c we transpose the board
    # before dealing with the vertical plays

    # Norvig says this makes calculate_score() brittle b/c
    # it's dependent on being called with ACROSS as the
    # direction the first time.
