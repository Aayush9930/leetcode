# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = self._isBalanced(root) 
        if x == -1:
            return False
        return True
    
    def _isBalanced(self, root):
        if not root:
            return 0 
        
        if not root.left and not root.right:
            return 1
        
        left_h = self._isBalanced(root.left)
        if left_h == -1:
            return -1

        right_h = self._isBalanced(root.right)
        if right_h == -1:
            return -1

        if abs(right_h - left_h) > 1:
            return -1

        return 1 + max(right_h, left_h)  


        

         