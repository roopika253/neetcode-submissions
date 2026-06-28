# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBST(self,root,min_value,max_value):
        if root == None:
            return True
        if not (min_value < root.val < max_value):
            return False
        left = self.isBST(root.left,min_value, root.val)
        right = self.isBST(root.right,root.val, max_value)
        if left and right:
            return True
        else :
            return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root,float("-infinity"), float("infinity"))
        