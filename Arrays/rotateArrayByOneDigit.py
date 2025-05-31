


def rotateArrayByOneDigit(arr):
    if not arr:
        return 0  # O(1)
    temp =  arr[0] # O(1)
    for i in range(1,len(arr)): #O(n-1) ~ O(n)
        arr[i-1] = arr[i]# O(1)
    arr[-1] = temp # O(1)

# total complexity  = O(1) + O(1) + O(n) + O(1) + O(1) = O(n) 
    return arr

print(rotateArrayByOneDigit([2,3,1,4,3,5,8]))
