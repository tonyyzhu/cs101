# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    i = len(s)
    j = 0
    k = -1
    while j + 1 <= i/2:
        if s[j] == s[k]:
            j = j + 1
            k = k - 1
        else:
            return False
    return True

# Above work because strong position starts from zero, and ened with -1. But, empty string and single letter are all true.


#print is_palindrome('')
#>>> True
#print is_palindrome('abab')
#>>> False
#print is_palindrome('abba')
#>>> True