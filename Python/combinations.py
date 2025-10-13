class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def recursive(start, depth):
            result = []
            if depth == 1: return [[start]]
            
            for i in range(start+1, n+1):
                smallCombs = recursive(i, depth-1)
                for comb in smallCombs:
                    comb.append(start)
                    result.append(comb)

            return result

        if k == 1:
            for i in range(n):
                result.append([i+1])
            return result

        for i in range(n-1):
            for x in recursive(i + 1, k):
                result.append(x)

        return result

