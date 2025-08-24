from xmlrpc.client import MININT


def second_largest(arr):
    s_largest=MININT
    largest=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            s_largest=largest
            largest=arr[i]
        if s_largest<largest and s_largest>arr[i] :
            s_largest=arr[i]
    return s_largest

print(second_largest([1,2,3,4,5,6,7]))

