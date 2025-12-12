# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = {}
        def dfs(root, row, col):
            if not root:
                return 
            
            if col not in h:
                h[col] = []
            
            h[col].append((row, root.val))
        
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
        
        dfs(root, 0, 0)

        #-1 : [9]
        # 0: [3, 15]
        for col in h:
            h[col].sort()

        res = [] 
        for key, val in h.items():
            res.append((key, val))
        
        res.sort()
        out = [[v for r, v in pairs] for col, pairs in res]
        return out