# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def makeTree(l ,r):
            if l > r:
                return None
            
            mid = (r + l) // 2
            root = TreeNode(nums[mid])
            root.left = makeTree(l, mid - 1)
            root.right = makeTree(mid + 1, r)
            return root
        
        return makeTree(0, len(nums) - 1)
