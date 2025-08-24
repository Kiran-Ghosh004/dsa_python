def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]  # overwrite instead of swap
            i += 1
    return i + 1  # length of unique part


nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6]
length = remove_duplicates(nums)
print(length)  # 6
print(nums[:length])  # [1, 2, 3, 4, 5, 6]

