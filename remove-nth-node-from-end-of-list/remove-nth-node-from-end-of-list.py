# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast_ptr = dummy
        slow_ptr = dummy
        while fast_ptr.next:
            n -= 1
            fast_ptr = fast_ptr.next
            if n < 0:
                slow_ptr = slow_ptr.next
​
        slow_ptr.next = slow_ptr.next.next
        
        return dummy.next
​
