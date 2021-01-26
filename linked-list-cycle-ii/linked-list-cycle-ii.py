# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        cycle = False
        while second.next and second.next.next:
            second = second.next.next
            first = first.next
            
            if first == second:
                cycle = True
                break
        
        if cycle:
            first = dummy
            while first != second:
                first = first.next
                second = second.next
                
        return first if cycle else None
