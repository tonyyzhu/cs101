# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

# my original solution
# def hash_string(keyword,buckets):
 #   i = 0
 #   j = 0
 #   while i<len(keyword):
 #       j= j + ord(keyword[i])
 #       i = i + 1
 #   return (j % buckets)


# I don't understand the way this for loop works - it is add sum of modulus together
# Could it have a possible of that sum > operator?
# I understand the while loop BTW, which has no amigubity

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        print "s", ord(s) % buckets
        out = (out + ord(s)) % buckets
        print "Out:", out
    return out

print "hash_string", hash_string ("Lilith", 5)

def hash_string2(keyword,buckets):
    i = 0
    j = 0
    while i<len(keyword):
        j= j + ord(keyword[i])
        i = i + 1
    return (j % buckets)

print "hash_string2 ", hash_string2 ("Lilith", 5)

print 100 % 6

print ((((((((((((((((20 % 6) + 10) % 6  + 10) % 6 )  + 10) % 6 ) + 10) % 6 )  + 10) % 6 ) + 10) % 6 ) + 10) % 6 ) + 10) % 6 ) % 6

