def majorityElement(arr):

# = [1,1,3,2,2,5,5,5,2]

    element = None
    counter = 0
    for i in range(len(arr)):
        if counter == 0:
            element = arr[i]
        if arr[i] == element:
            counter +=1
        if arr[i] != element:
            counter -=1
    
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == element:
            cnt +=1
    

    if cnt > len(arr)//2:
        print(element)
    else:
        print("none")
        


# majorityElement([2,2,1,1,1,2,2])



# optimized 


def majorityElement_O(nums):

    element = None
    counter = 0


    for i in nums:
        if counter == 0:
            element = i 
        counter+=1 if i == element else -1
    
    return element # this is when you are sure that element will surely exist in array

print(majorityElement_O([2,2,1,1,1,2,2]))