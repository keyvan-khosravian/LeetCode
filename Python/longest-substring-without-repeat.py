class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l, res = 0, 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])∏
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res