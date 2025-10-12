# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res = []

        q = collections.deque()
        q.append(root)        

        while q:
            qLen = len(q)
            sum = 0

            for i in range(qLen):
                node = q.popleft()
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(float(sum) / qLen)
        
        return res