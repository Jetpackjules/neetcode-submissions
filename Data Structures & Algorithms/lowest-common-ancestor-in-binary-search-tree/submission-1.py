# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # LCS traits: BETWEEN OR EQUAL TO P and Q!
        # edge: 1 size, same val, uelss not possible cuz unique and specifies TWO nodes, not ONE node effeed twice?

        if p == q:
            return p
        
        #  no need for recursion i think, just probe?
        if p.val < q.val:
            low, hi = p, q
        else:
            low, hi = q, p

        curr = root
        while not low.val <= curr.val <= hi.val:
            if low.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            

        return curr
