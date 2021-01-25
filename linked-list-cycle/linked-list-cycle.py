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
        
        node = dummy
        while node:
            node = node.next
            if node in seen:
                return True
            else:
                seen.add(node)
        return False
