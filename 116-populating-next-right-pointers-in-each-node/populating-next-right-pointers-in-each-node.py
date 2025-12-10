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
        if root == None:
            return root
        
        q = deque([(root, 0)])

        while q:
            n, l = q.popleft()

            if n.left:
                q.append((n.left, l + 1))
            if n.right:
                q.append((n.right, l + 1))

            curr = n
            while q and q[0][1] == l:
                new, l = q.popleft()
                if new.left:
                    q.append((new.left, l + 1))
                if new.right:
                    q.append((new.right, l + 1))
                curr.next = new
                curr = new
            curr.next = None

        return root
