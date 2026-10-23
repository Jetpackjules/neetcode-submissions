# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # to remove:
        # make curr point to next next?

        # edge:
        # removing after end OOB: issue
        # removing very first: just update head.

        # N from end:

        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1
        
        temp_head = ListNode(0, head)
        curr = temp_head
        i = -1
        while i < size-n-1:
            i += 1
            curr = curr.next
        
        curr.next = curr.next.next


        return temp_head.next
        


        