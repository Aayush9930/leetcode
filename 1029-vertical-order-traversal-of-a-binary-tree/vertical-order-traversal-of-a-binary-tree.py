# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = {}
        col_map = defaultdict(list)  # col -> list of (row, val)
        def dfs(node, row, col):
            if not node:
                return 

            if col in out:
                out[col].append(node.val)
            else:
                out[col] = [ node.val ]
                
            col_map[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        res = []
        for col in sorted(col_map.keys()):                               # sort columns
            pairs = sorted(col_map[col], key=lambda x: (x[0], x[1]))     # sort by row, then val
            res.append([val for _, val in pairs])
        return res

            

            




    