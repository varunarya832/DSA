def main():
    arr = [0,1,0,3,12]
    arr = moveZerosToEnd(arr)
    print(arr)

def moveZerosToEnd(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pointer] = arr[i]
            pointer +=1
        # final temp arr [1,3,12,3,12]

    while pointer < len(arr): # 3 < 5 ; 2 runs
        arr[pointer] = 0
        pointer +=1

    return arr

main()


# Complexity
    # Time : for i in range(len(arr)): runs for n times 
                # performs constant operations for n time like , comparsion,assignment and increment
                        # O(n)
    #        : while pointer < len(arr): runs for n times for worst case 
                    # with constant operations like assignment and increment 
                        # O(n)

    # Time complexity : O(n) + O(n) = O(n)

    # Space Complexity = O(1) (constant space)
