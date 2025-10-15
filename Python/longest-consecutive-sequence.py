class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        s = set(nums)

        for num in s:
            if num - 1 not in s:
                current_num = num
                longest = 1

                while current_num + 1 in s:
                    longest += 1
                    current_num += 1

                result = max(result, longest)

        return result