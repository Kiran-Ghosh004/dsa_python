def move_zeroes(arr, n):
    j = -1
    # Step 1: Find index of first zero
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    # If no zero found, nothing to do
    if j == -1:
        return arr

    # Step 2: Move non-zero elements forward
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


# Example
arr = [1, 0, 2, 0, 3, 4, 0, 5]
print(move_zeroes(arr, len(arr)))
# [1, 2, 3, 4, 5, 0, 0, 0]
