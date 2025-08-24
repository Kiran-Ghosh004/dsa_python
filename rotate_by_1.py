def rotate(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp

arr1=[1,2,3,4,5,6]
rotate(arr1)
print(arr1)