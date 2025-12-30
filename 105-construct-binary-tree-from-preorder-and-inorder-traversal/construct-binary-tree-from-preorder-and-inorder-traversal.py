# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder == [] and inorder == []:
            return None
        
        root = TreeNode(preorder[0])

        target_i = None
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                target_i = i
                break

        root.left = self.buildTree(preorder[1: i + 1], inorder[ : target_i ])

        root.right = self.buildTree(preorder[i + 1:], inorder[ target_i + 1: ])

        return root