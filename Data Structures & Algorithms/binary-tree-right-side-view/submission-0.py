# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                top = queue.popleft()
                temp.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            ans.append(temp[-1])
        return ans
        