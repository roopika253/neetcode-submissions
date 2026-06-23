# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root):
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        diameter = left+right
        sub = max(self.dfs(root.left),self.dfs(root.right))
        return max(diameter,sub)

    def height(self,root):
        if root == None:
            return 0
        return 1+ max(self.height(root.left),self.height(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
        
       
        