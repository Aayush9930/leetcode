# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBst(root, float('-inf'), float('inf'))
    
    def _isValidBst(self, root, l, h):
        if not root:
            return True
        
        if not ( l < root.val < h ):
            return False
        
        return self._isValidBst(root.left, l, root.val) and self._isValidBst(root.right, root.val, h)
    
