# Implement a function that:
# 1. Is named avg
# 2. Takes a variable number of integer arguments; it is guaranteed
# that at least one argument will be passed
# 3. Returns the average value of the passed arguments as a float
# The implementation will be tested by a provided code stub on several
# input files. Each input file contains one line with space-separated
# arguments for the function. The function will be called with those
# arguments, and the returned result will be printed to the output with
# exactly 2 decimal places.
# Example
# 3 arguments are read and passed to the function: 1, 2, and 3. The
# average is calculated to be (1 + 2 + 3) / 3 = 2.00. This is then returned
# as a float to be printed.
# Constraints
# 1 ≤ number of arguments for the function ≤ 100
# -100 ≤ value of passed arguments ≤ 100

def avg(*n):
    sums = 0
 
    for t in n:
        sums = sums + t
 
    avg = sums / len(n)
    return avg

# Driver Code
result1 = avg(1, 2, 3)
result2 = avgfun(2, 6, 4, 8)
 
# Printing average of the list
print(round(result1, 2))
print(round(result2, 2))
