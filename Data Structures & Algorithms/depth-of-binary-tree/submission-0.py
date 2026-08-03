# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #  edge cases:
        # empty
        # depth =1?
        # no ned to pass var, can update absolutely, so no return statement
        # still have to pass var in, to maintain count
        dep = 0

        def probe(root, count):
            nonlocal dep
            if not root:
                dep = max(dep, count)
            else:
                count += 1
                probe(root.left, count)
                probe(root.right, count)
                
            
        
        probe(root, 0)
        return dep

        