# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        hm = {}
        for i in range(n):
            hm[inorder[i]] = i
        self.ptr = 0
        def dfs(l,r):
            if l > r:
                return None
            node = TreeNode(preorder[self.ptr])
            index = hm[preorder[self.ptr]]
            self.ptr += 1
            node.left = dfs(l, index -1)
            node.right = dfs(index + 1, r)
            return node
           
            
        return dfs(0, n-1)
        