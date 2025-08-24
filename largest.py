def largest(arr):
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

print(largest([2,3,9,4,6,7]))