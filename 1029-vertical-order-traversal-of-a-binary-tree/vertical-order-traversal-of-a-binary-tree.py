# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.h = defaultdict(list) # col => [root vals]
        def dfs(node, row, col):
            if not node:
                return 
            self.h[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row +1, col + 1)
        dfs(root, 0, 0)

        min_col = min(self.h.keys())
        out = []
        while min_col in self.h:
            x = sorted(self.h[min_col])
            y = [ v for r, v in x ]
            out.append(y)
            min_col += 1
        return out
