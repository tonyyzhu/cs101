#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

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






#print fibonacci(36)
#>>> 14930352