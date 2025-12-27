"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
            
        tree = []
        q = deque([(root, 0)])

        while q:
            n, l = q.popleft()
            if len(tree) == l:
                tree.append([])
            tree[l].append(n)

            if n.left:
                q.append((n.left, l + 1))
            
            if n.right:
                q.append((n.right, l + 1))

        for layer in tree:
            for i in range(len(layer)):
                layer[i].next = layer[i + 1] if i + 1 < len(layer) else None
        
        return root