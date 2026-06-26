# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs2(self,root,subroot):
        if root == None and subroot == None:
            return True
        if root and subroot:
            if root.val == subroot.val:
                return (self.dfs2(root.left, subroot.left)) and ((self.dfs2(root.right, subroot.right)))
            else :
                return False
        else :
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs1(root, subroot):
            if root == None and subroot == None:
                return True
            if root and subroot:
                if root.val == subroot.val and self.dfs2(root,subroot):
                    return True
                return (dfs1(root.left,subroot)) or (dfs1(root.right,subroot))
            else :
                return False
        return dfs1(root,subRoot)

        