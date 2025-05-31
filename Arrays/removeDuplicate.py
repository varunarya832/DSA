
# arr = [1,1,2,3,3,4,5,6]

def removeDuplicateFromSortedArray(arr):

    if len(arr) < 0:
        return 0

    pointer = 0
    for i in range(len(arr)):
        if arr[i] != arr[pointer]:
            pointer +=1
            arr[pointer] = arr[i]
    return pointer+1


print(removeDuplicateFromSortedArray([1,1,2,3,3,4,5,6]))