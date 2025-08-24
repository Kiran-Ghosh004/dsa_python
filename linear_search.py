def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return True
    return False

print(linear_search([1,2,3,4,5,6],5))
