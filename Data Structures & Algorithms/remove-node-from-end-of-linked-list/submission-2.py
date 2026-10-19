# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start = dummy
        finish = head

        while n > 0:
            finish = finish.next
            n = n - 1
        
        while (finish!=None):
            start = start.next
            finish = finish.next
        
        start.next = start.next.next
        return dummy.next
