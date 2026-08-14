# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        

        # approach:
        # 1 reverse? cant thats O(n) space!
        #  ONLY REVERSE SECOND HALF!
        def reverse(prev: ListNode, head: ListNode):
            prev = None
            curr = head
            while curr:
                temp_ = curr.next
                curr.next = prev
                prev = curr
                curr = temp_
            return prev


        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        back = reverse(None, slow)

        # now merge:
        curr = head
        while back.next:
            temp_ = curr.next
            btemp_ = back.next

            curr.next = back
            back.next = temp_
            curr = temp_


            back = btemp_
