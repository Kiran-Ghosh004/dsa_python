

def missing_number(arr):
    n = len(arr)  # length of given array
    total = (n + 1) * (n + 2) // 2  # expected sum from 1 to n+1
    actual_sum = sum(arr)
    return total - actual_sum

print(missing_number([1,3,4,5]))  # Output -> 2
