# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            right = None

            for i in range(len(queue)):
                cur = queue.pop(0)

                if cur:
                    right = cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            if right:
                res.append(right.val)
        return res