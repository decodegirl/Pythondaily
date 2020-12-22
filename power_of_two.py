def isPowerOfTwo(n):
    if n < 0: #if num  is less than zero that means its a negative hence not a power of 2
        return False
    while n % 2 == 0:
        n = n/2 #divide by two
    return n == 1 # if n == 1 then num is a power of 2 hence return true, otherwise false


