lookup_table = {}

# Non-memoized version
def factorial(n):
    if n is 0:
        print("Inside Main for --> ", n)
        return 1
    else:
        print("Inside Else for --> ", n)
        return factorial(n - 1) * n

print(factorial(3))

###############################################################################

#memoized Version
def factorial_mem(n):
    if n is 0:
        print("Inside Main for --> ", n)
        return 1
    elif n in lookup_table:
        print("Inside Memory for --> ", n)
        return lookup_table[n]
    else:
        print("Inside Else for --> ", n)
        x = factorial_mem(n - 1) * n
        lookup_table[n] = x
        return x
    
print(factorial_mem(5))

print(factorial_mem(4))

print(factorial_mem(7))

lookup_table
###############################################################################