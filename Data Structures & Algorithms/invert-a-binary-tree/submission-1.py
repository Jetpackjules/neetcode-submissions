# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #  edge cases: empty, suymmetric, etc
        if not root:
            return
        def probe(root):
            if root.left:
                probe(root.left)
            if root.right:
                probe(root.right)
            root.left, root.right = root.right, root.left
        
        probe(root)
        return root