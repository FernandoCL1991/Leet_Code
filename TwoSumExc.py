## Leet Code, ex. 1: "Two Sum"

# Given an list of numbers, look for all the sum cobinations to reach for the target
nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   

# --> Nice Approach
    complementMap = dict() ## Map function, return just the complement number and its index to add up to reach the target
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            
            if num in complementMap: 
                return [complementMap[num], i]
            else:
                complementMap[complement] = i

# --> Bruteforce Approach
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
    def bruteForceTwoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i, j]