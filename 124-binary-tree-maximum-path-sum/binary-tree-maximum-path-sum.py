# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float('-inf')

        def dfs(root):
            if not root:
                return 0 
            
            if not root.left and not root.right:
                self.maximum = max(self.maximum, root.val)
                return root.val
            
            left_path = dfs(root.left)
            right_path = dfs(root.right)

            if left_path >= 0 and right_path >= 0:
                self.maximum = max(self.maximum, left_path + root.val + right_path)
                return root.val + max(left_path, right_path)
            
            elif left_path >= 0:
                self.maximum = max(self.maximum, left_path + root.val)
                return root.val + left_path
            
            elif right_path >= 0:
                self.maximum = max(self.maximum, right_path + root.val)
                return root.val + right_path

            elif left_path < 0 and right_path < 0:
                self.maximum = max(self.maximum, root.val)
                return root.val
        
        dfs(root)
        return self.maximum