class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # build all possible subarrays
        # keep ones that sum to target
        # pick smallest one
        result = float("inf")

        l, sum = 0, 0

        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                result = min(r - l + 1, result)
                sum -= nums[l]
                l += 1
        
        return 0 if result == float("inf") else result