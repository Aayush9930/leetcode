# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n


        q = deque([(root, 1)])

        while q:
            n, l = q.pop()

            if l == depth - 1:
                temp_left = n.left
                temp_right = n.right
                n.left = TreeNode(val)
                n.right = TreeNode(val)
                n.left.left = temp_left
                n.right.right = temp_right

            if n.left:
                q.append((n.left, l + 1))
                
            if n.right:
                q.append((n.right, l + 1))
        return root