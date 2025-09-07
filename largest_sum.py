def largest_sum(arr):
    sum=0
    smallest=arr[0]
    for i in arr:
        sum +=i
        if i<smallest:
            smallest=i

    return sum-smallest


print(largest_sum([3,8,6,9,2]))

def largest_sum2(arr2):
    arr2.sort()
    sum=0
    for i in range(1,len(arr2)):
        sum+=arr2[i]
    return sum

print(largest_sum2([3,8,6,9,2]))


