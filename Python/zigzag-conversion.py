class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s

        res = ""        
        for row in range(numRows):
            increment = 2 * (numRows - 1)

            i = row
            while i < len(s):
                res += s[i]

                if (row > 0 and row < numRows - 1 and (i+increment-2*row) < len(s)):
                    res += s[i + increment - 2 * row]

                i += increment

        return res