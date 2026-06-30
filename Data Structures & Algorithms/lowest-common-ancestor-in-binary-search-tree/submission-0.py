# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findpath(self, root, target , temp):
        if root == None:
            return
        if target.val < root.val:
            self.findpath(root.left , target , temp +[root] )
        elif target.val > root.val:
            self.findpath(root.right , target , temp +[root])
        else :
            temp.append(root)
            self.path.append(temp)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.path = []
        self.findpath(root, p, [])
        self.findpath(root, q, [])
        path1 = self.path[0]
        path2 = self.path[1]
        n = len(path1)
        m = len(path2)
        i = 0
        j = 0
        ans = None
        while i < n and j < m:
            if path1[i] == path2[j]:
                ans = path1[i]
            i += 1
            j += 1
        return ans



        