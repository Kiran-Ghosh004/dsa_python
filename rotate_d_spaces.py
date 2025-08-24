def rotate(arr,d):
    temp=[]
    n=len(arr)
    for i in range(d):
        temp.append(arr[i])
    for j in range(d,n):
        arr[j-d]=arr[j]
    for k in range(n-d,n):
        arr[k]=temp[k-(n-d)]

arr1=[1,2,3,4,5,6,7]
rotate(arr1,3)
print(arr1)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_d(arr,d):
    d=d%len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,len(arr)-1)
    reverse(arr,0,len(arr)-1)

arr2=[1,2,3,4,5,6,7]
rotate_d(arr2,3)
print(arr2)




