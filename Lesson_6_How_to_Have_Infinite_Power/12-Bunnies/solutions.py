def fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

# From the README:
# We do NOT accept pull requests that have deleted another contributer's hint or solution without a very clear reason
# ALL solutions must be clearly documented
# ALL solutions must actually work
# ONLY use concepts covered in the class so far
