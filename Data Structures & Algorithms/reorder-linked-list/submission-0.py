# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         l1 = ListNode()
         l2 = ListNode()

         if head is None:
            return 

         slow = head
         fast = head.next

         while fast and fast.next is not None:
            slow =slow.next
            fast = fast.next.next
         l2 = slow.next
         slow.next = None
         l1 = head
         
         if l2 is None:
            return
          
         curr = l2
         prev = None
         while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
         l2 = prev

         dummy = ListNode()
         tail = dummy
         l_1 = l1
         l_2 = l2
        

         while l_1 and l_2 is not None:
             l1_next = l_1.next
             l2_next = l_2.next
             tail.next =l_1
             l_1.next = l_2
             l_1 = l1_next
             tail = tail.next
             l_2.next = l_1
             l_2 = l2_next
             tail = tail.next
         return 
    
          


