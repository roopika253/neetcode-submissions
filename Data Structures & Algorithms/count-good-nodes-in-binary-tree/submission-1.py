# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, max_value):
        if root == None:
            return 0
        if root.val >= max_value:
            max_value = root.val
        left = self.dfs(root.left, max_value)
        right = self.dfs(root.right, max_value)
        if root.val >= max_value:
            return 1 + left + right
        else :
            return left + right
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root,root.val)
     
        