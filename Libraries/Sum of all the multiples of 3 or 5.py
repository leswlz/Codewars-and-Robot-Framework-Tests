# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Your task is to write function findSum.
# Up to and including n, this function will return the sum of all multiples of 3 and 5.
# For example:
# findSum(5) should return 8 (3 + 5)
# findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def find(n):
    result_sum = 0
    for i in range(0, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            result_sum += i
    return result_sum


find(5)
find(10)
