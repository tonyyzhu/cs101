 def is_palindrome(s):
 +    i = len(s)
 +    j = 0
 +    k = -1
 +    while j + 1 <= i/2:
 +        if s[j] == s[k]:
 +            j = j + 1
 +            k = k - 1
 +        else:
 +            return False
 +    return True
 +
 +# Above work because strong position starts from zero, and ened with -1. But, empty string and single letter are all true.

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far
