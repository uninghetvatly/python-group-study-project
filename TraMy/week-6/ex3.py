# Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)

                # TODO: thêm node.val vào level
                level.append(node.val)
                # TODO: nếu node.left thì thêm vào queue
                if (node.left):
                    queue.append(node.left)
                # TODO: nếu node.right thì thêm vào queue
                if (node.right):
                    queue.append(node.right)
            result.append(level)

        return result
        