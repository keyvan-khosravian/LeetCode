class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        o = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if result and result[len(result) - 1] != ' ':
                    result.append(' ')
                    o = len(result)
                else:
                    continue
            else: 
                result.insert(o, s[i])

        if result[len(result) - 1] == ' ':
            result.pop()
            
        return ''.join(result)