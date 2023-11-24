# This function locates two numbers within an array of numbers that sum to a given value.

def twoSum(nums, val):
    num_map = {} # Maps each num
    n = len(nums) 
    
    for i in range(n): 
        complement = val - nums[i] # The current number's complement to add to the val
        if complement in num_map: 
            return [i, num_map[complement]] # Return both indicies if complement exists
        num_map[nums[i]] = i # Otherwise, map the number to its index
        
    return [] # Return nothing if no such pair exists.