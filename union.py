def union(arr1, arr2):
    union_arr = []
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(union_arr) == 0 or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
        else:
            # arr1[i] == arr2[j]
            if len(union_arr) == 0 or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements
    while i < n1:
        if union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1

    while j < n2:
        if union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1

    return union_arr

# Example
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5, 6]
print(union(arr1, arr2))  # [1, 2, 3, 4, 5, 6]
