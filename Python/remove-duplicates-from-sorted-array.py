class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        i, removals = 0, 0

        while i < len(nums) -1 - removals:
            if nums[i] == nums[i + 1]:
                toMove = 0
                for j in range(i + 2, len(nums)):
                    if nums[j] == nums[i]: toMove += 1

                for k in range(toMove):
                    l = i + 2
                    r = l + 1
                    while r < len(nums):
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        r += 1
                removals += toMove
                i += 2
            else:
                i += 1

        return len(nums) - removals
