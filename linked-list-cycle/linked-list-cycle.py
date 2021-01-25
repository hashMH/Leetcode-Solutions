# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode(0)
        dummy.next = head
        
        seen = set()
        
        fast_ptr = dummy
        slow_ptr = dummy
        while fast_ptr.next and fast_ptr.next.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True
        return False
