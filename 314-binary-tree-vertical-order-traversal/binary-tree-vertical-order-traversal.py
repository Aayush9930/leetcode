# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        h = defaultdict(list)

        def dfs(root, row, col):
            if not root:
                return 
            
            h[col].append((row, root.val))
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)

        dfs(root, 0, 0)

        x = min(h.keys())
        out = []
        while x in h:
            arr = [ v for r, v in sorted(h[x], key = lambda t: t[0])]
            out.append(arr)
            x += 1
        
        return out


