def fibonacci(n):
    x = 0
    y = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        i = 0
        z = 0
        while i < n - 1:
            z = x + y
            x = y
            y = z
            i = i + 1
    return z

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far
