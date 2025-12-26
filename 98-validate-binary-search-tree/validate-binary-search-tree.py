# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.out = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.out.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(self.out)):
            if self.out[i - 1] >= self.out[i]:
                return False
        return True 




    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self._isValidBST(root, float('-inf'), float('inf'))

    # def _isValidBST(self, root, low, high):
    #     if not root:
    #         return True
        
    #     if not (low < root.val < high):
    #         return False
        
    #     return self._isValidBST(root.left, low, root.val) and self._isValidBST(root.right, root.val, high)
