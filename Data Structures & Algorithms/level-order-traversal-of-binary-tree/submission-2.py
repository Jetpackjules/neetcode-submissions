# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        out = []
        def recurse(root, depth: int = 0):
            if root:
                if len(out) <= depth:
                    out.append([root.val])
                else:
                    out[depth].append(root.val)
            
                recurse(root.left, depth+1)
                recurse(root.right, depth+1)


        recurse(root)
        return out
        