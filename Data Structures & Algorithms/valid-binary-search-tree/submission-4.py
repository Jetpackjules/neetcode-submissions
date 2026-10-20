# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(root: TreeNode, mm: tuple):
            if root:
                if not (mm[0] < root.val < mm[1]):
                    return False
                return recurse(root.left, (mm[0], root.val)) and recurse(
                    root.right, (root.val, mm[1])
                )

            else:
                return True

        return recurse(root, (float("-inf"), float("inf")))
