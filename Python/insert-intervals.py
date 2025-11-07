class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        result = []

        if len(intervals) == 0: return [newInterval]

        for i in range(len(intervals)):
            if intervals[i][0] < newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]

            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])

            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result
