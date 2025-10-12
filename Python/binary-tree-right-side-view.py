from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def makeNextLevel(level):
            result = []
            for node in level:
                if node.left: result.append(node.left)
                if node.right: result.append(node.right)
            return result

        if not root: return []

        result = []
        level = [root]

        while level:
            result.append(level[len(level) - 1].val)
            level = makeNextLevel(level)

        return result