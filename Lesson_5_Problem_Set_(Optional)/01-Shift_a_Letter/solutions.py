# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    if letter <> 'z':
        return str(unichr(ord(letter)+1))
    else:
        return 'a'


print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a