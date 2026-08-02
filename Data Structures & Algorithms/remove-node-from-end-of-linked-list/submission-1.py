# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = ListNode(0,head)
        if head is None:
            return 

        dummy = second
        while n!=0:
            first = first.next
            n = n-1
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

