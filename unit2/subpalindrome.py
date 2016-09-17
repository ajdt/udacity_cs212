# Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.lower()
    if len(text) == 1:
        return True
    candidates , c2 = get_candidates(text), []
    for pair in candidates:
        while pair[0] > 0 and pair[1] < len(text) and text[pair[0] - 1] == text[pair[1]]:
            pair = (pair[0] - 1, pair[1] + 1)
        c2 += [pair]
    if c2 == []:
        return (0, 0)
    return max(c2, key=maxPalindromeTuple)

def get_candidates(text):
     triples = [(l, l+3) for l in range(0, len(text) - 2) if isPalindrome(text[l:(l+3)])]
     doubles = [(l, l+2) for l in range(0, len(text) - 1) if isPalindrome(text[l:(l+2)])]
     return triples + doubles

def isPalindrome(text):
    return text == text[::-1]

def maxPalindromeTuple(tuple1 ):
    return (tuple1[1] - tuple1[0])

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

#print test()
text = 'Race carr'# " this is a racecar isso"
print get_candidates(text)
print "0"*10 +  "1"*10 + "2"*20
print "0123456789"*3
print text
print max( [( 1, 2), (9, 10), (1, 50), (99, 102)], key=maxPalindromeTuple)
print "****", longest_subpalindrome_slice(text)
