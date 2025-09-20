"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

You must write an algorithm with O(n) time complexity.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memory = {}

        for i, num in enumerate(nums):
            remainder = target - num;
            if remainder in memory:
                return [memory[remainder[remainder]], i]
            memory[num] = i;
        return []