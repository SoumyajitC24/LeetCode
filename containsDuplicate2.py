'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

Solution: Dictionary/HashTable
1. Enumerate the list to get index+numbers
2. If nummber not in Dictionary, add it as (key,value) = (num,index)
3. If number is present, check if difference with current_index is <=k, return True
4. Else, dict(num) = current index
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        answer = dict()
        for index, num in enumerate(nums):
            if num in answer:
                if index - answer[num] <= k:
                    return True
                answer[num] = index

            else:
                answer[num] = index
        
        return False
