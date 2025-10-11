class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def helper(num):
            if num == '1':
                return []
            if num == '2':
                return ['a', 'b', 'c']
            if num == '3':
                return ['d', 'e', 'f']
            if num == '4':
                return ['g', 'h', 'i']
            if num == '5':
                return ['j', 'k', 'l']
            if num == '6':
                return ['m', 'n', 'o']
            if num == '7':
                return ['p', 'q', 'r', 's']
            if num == '8':
                return ['t', 'u', 'v']
            if num == '9':
                return ['w', 'x', 'y', 'z']

        if not digits: return []
        if len(digits) == 1:
            return helper(digits[0])

        output = []
        for ch in helper(digits[0]):
            for comb in self.letterCombinations(digits[1:]):
                output.append(ch + comb)


        return output

        