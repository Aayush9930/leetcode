# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.path_finder(root, p)
        path_q = self.path_finder(root, q)

        s = set(path_p)
        for n in path_q:
            if n in s:
                return n
        

    def path_finder(self, root, target):
        if not root:
            return None
        
        if root.val == target.val:
            return [ root ]
        
        left_path = self.path_finder(root.left, target)
        right_path = self.path_finder(root.right, target)

        if left_path == None and right_path == None:
            return None 
        
        if left_path:
            left_path.append(root)
            return left_path
        
        if right_path:
            right_path.append(root)
            return right_path