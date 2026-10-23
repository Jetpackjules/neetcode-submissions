# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # to remove:
        # O(n), O(1)

        # Edge case: first node to be removed: n=size

        # sol:
        # Have a fast point n steps ahead of curr, so we know when curr is to be replaced:


        # init fast ahead:
        pre = ListNode(0, head)

        fast = curr = pre

        for i in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            curr = curr.next
        
        curr.next = curr.next.next
        return pre.next
        


        