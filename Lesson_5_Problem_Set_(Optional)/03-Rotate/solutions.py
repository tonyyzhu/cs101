# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(key, n):
    # Your code here
    result = ''
    if key == '':
        return ''
    else:
        for letter in key:
            if letter ==' ':
                result = result + ' '
            else:
                result = result + shift_n_letters(letter, n)
        return result

def shift_n_letters(letter, n):
    if (ord(letter) + n) >= 97:
        if (ord(letter) + n) <= 122:
            return str(unichr((ord(letter) + n )))
        else:
            return str(unichr((ord(letter) + n - 122 + 96)))
    else:
        return str(unichr((ord(letter) + n + 122 - 96)))


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> if)your)code)works)correctly)you)should)be)able)to)read)this
print rotate("this course teaches you to code",
    7)
#>>>aopz jvbyzl alhjolz fvb av jvkl