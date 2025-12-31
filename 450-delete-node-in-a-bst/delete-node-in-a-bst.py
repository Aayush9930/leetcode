# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # find the node
        # replace it with the leftmost value of the right subtree

        if not root:
            return root

        if key == root.val:
            # if i do not have left child
            if not root.left:
                return root.right
            # if i do not have right child
            if not root.right:
                return root.left
            
            # if i have both
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val, curr.val = curr.val, root.val
            root.right = self.deleteNode(root.right, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root
