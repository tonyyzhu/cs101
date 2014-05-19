# Please write SOLUTIONS here

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far

def rabbits(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n <= 5:
        return (rabbits(n-1) + rabbits(n-2))
    return (rabbits(n-1) + rabbits(n-2) - rabbits(n-5))
