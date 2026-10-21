# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Nlogn sol: turn into list, sort list, return index! easy

        # logn sol, traverse tree, tunn into list from lo->hi
        # traversal: left child, self, right child, ascend!
        # i = k
        out = []
        def recurse(root: Optional[TreeNode]):
            if not root:
                return

            recurse(root.left)
            print(root.val)
            out.append(root.val)

            recurse(root.right)

        recurse(root)
        return out[k-1]

            
        
        