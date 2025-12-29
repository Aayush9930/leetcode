# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        out = []
        q = deque([(root, 0)])

        while q:
            n, l = q.popleft()

            if len(out) == l:
                out.append([])
            
            out[l].append(n.val)

            if n.left:
                q.append((n.left, l + 1))
            
            if n.right:
                q.append((n.right, l + 1))
            
        return out

