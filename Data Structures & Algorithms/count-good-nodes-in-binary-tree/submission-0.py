# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, max_value):
        if root == None:
            return 
        if root.val >= max_value:
            max_value = root.val
            self.ans += 1
        self.dfs(root.left, max_value)
        self.dfs(root.right, max_value)
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root,root.val)
        return self.ans
        