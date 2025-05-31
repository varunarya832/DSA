def rotate_array_to_left_by_1(arr,k):
    """ 
    1 . Brute Force Approach
    Rotate the array to the right by k steps.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # arr = [0,1,2,3,4]
    temp = arr[0]
    
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = temp
    
    return arr

# print(rotate_array_to_left([0,1,2,3,4],1))



def rotate_array_to_left_by_k(arr,k):
    """ 
    1 . Brute Force Approach
    Rotate the array to the right by k steps.
    Time Complexity: O(n*k)
    Space Complexity: O(1)
    """
    # arr = [0,1,2,3,4]
    k = k%len(arr)
    for j in range(0,k):
        temp = arr[0]
        for i in range(1,len(arr)):
            arr[i-1] = arr[i]
        arr[-1] = temp
    return arr

# print(rotate_array_to_left_by_k([0,1,2,3,4],34))
        
        
def rotate_array_to_right_by_1(arr,k):
    """ 
    1 . Brute Force Approach
    Rotate the array to the right by k steps.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # arr = [0,1,2,3,4]
    
    """
    
    In case of right , we will move one element from right side , 
    i arr[] 4 is on right side , so we will move this element 
    """
    temp = arr[-1]
    
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    
    return arr

# print(rotate_array_to_right_by_1([0,1,2,3,4],1))



def rotate_array_to_right_by_k(arr,k):
    """ 
    1 . Brute Force Approach
    Rotate the array to the right by k steps.
    Time Complexity: O(n*k)
    Space Complexity: O(1)
    """
    # arr = [0,1,2,3,4]
    k = k%len(arr)
    for j in range(0,k):
        temp = arr[-1]
        for i in range(len(arr)-1 , 0 , -1):
            arr[i] = arr[i-1]
        arr[0] = temp
    return arr

# print(rotate_array_to_left_by_k([0,1,2,3,4],2))





def rotate_array_to_left_by_k_by_extra_space(arr , k):
    """
    - the approach is to use the extra spaces 
    here catch is , copy all the element from k psostion to n in the start
    """


    extra_space = [0] * len(arr) 
    
    for i in range(k , len(arr)):
        extra_space[i - k] = arr[i]
    
    for i in range(0,k):
        extra_space[(len(arr)-k)+1] = arr[i]
    
    for i in range(0,len(extra_space)):
        arr[i] = extra_space[i]
    return arr


# print(rotate_array_to_left_by_k_by_extra_space([0,1,2,3,4],2))
    
    
    
    
    

def rotate_array_to_right_by_k_by_extra_space(arr, k):
    """
    Rotates an array to the right by k positions using extra space.
    """
    n = len(arr)
    k = k % n  # Handle k > n

    extra_space = [0] * n

    # [1,2,3,4,5]
    # Copy last k elements to the beginning
    for i in range(k):
        extra_space[i] = arr[n - k + i]

    # Copy the first (n - k) elements after that
    for i in range(n - k):
        extra_space[k + i] = arr[i]

    return extra_space

# Test
# print(rotate_array_to_right_by_k_by_extra_space([ 1, 2, 3, 4,5], 2))




class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)

        self.r(nums , 0 , n-1 )
        self.r(nums , k , n - 1)
        self.r(nums ,0 ,  k -1)

        return nums






    def r(self , nums:List[int] , start:int , end:int ):
        while(start < end):
            nums[start]  , nums[end] = nums[end] , nums[start]
            start +=1
            end -=1
        return nums
    
        













        
        
    
    
    