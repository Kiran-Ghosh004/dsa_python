

def missing_number(arr):
    n = len(arr)  # length of given array
    total = (n + 1) * (n + 2) // 2  # expected sum from 1 to n+1
    actual_sum = sum(arr)
    return total - actual_sum

print(missing_number([1,3,4,5]))  # Output -> 2


def missing(arr):
    n = len(arr)
    # Create a hash array of size n+1 (0 to n)
    hash_arr = [0] * (n + 1)

    # Mark existing numbers
    for num in arr:
        hash_arr[num] = 1

    # Find the missing number
    for i in range(n + 1):
        if hash_arr[i] == 0:
            return i

# Example
arr = [0, 1, 3, 4]
print(missing(arr))  # 2





