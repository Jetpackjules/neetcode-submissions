# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot:
            return True
        if not root or not subRoot:
            return False
        # process:
        # find where the root nodes match
        # check if chiodrne natchr ecusrively!

        # finding matching root:
        matches = []
        def find(root: TreeNode) -> Optional[TreeNode]:
            if root == None:
                return
            if root.val == subRoot.val:
                matches.append(root)
            find(root.left)
            find(root.right)
        find(root)
        print(len(matches))

        def same(root1: TreeNode, root2: TreeNode) -> bool:
            if not root1 and not root2:
                return True
            
            if not (root1 and root2) or root1.val != root2.val:
                return False
            

            return same(root1.left, root2.left) and same(root1.right, root2.right)

        return any([same(match, subRoot) for match in matches])

            

