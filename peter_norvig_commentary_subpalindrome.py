def pal(text):
    "Return (i,j) such that text[i:j] is the longest palindrome in text."
    ## I'll define the variables I'm looking for.
    ## I'll give them initial values that I know are valid
    ## (because even the empty string has a null substring).
    besti, bestj, longest = 0, 0, 0
    ## Let's take care of upper/lower case once and for all:
    text = text.lower()
    ## Then I'll define a loop in which I try to improve them.
    ## At this point I can write "return besti, bestj" at the bottom of my function.
    ## Here's what I'll do.  I'll look at the middle points of all
    ## subpalindromes, and then try to grow the subpalindrome out from there.
    ## The middle point is either a 0- or a 1-character subpalindrome.
    ## We need both because the answer might be even- or odd-lengthed.
    ## So, when we define i and j, we know text[i:j] is a palindrome.
    ## Why? because text[i:j] is 0 or 1 characters, and all 0 or 1-character
    ## strings are palindromes.  Then, if text[i-1] == text[j], and if
    ## we haven't hit either end yet, then we can expand i and j
    ## one out in either direction, making a palindrome that is 2 characters longer.
    ## Keep doing that as long as we can, and update besti, bestj, longest
    ## whenever we have a new longest slice.
    for mid in range(len(text)):
       for delta in (0, 1):
           i, j = mid, mid+delta
           while (i > 0 and j < len(text) and text[i-1] == text[j]):
               i, j = i-1, j+1
           if j - i > longest:
               besti, bestj, longest = i, j, j - i
return besti, bestj

