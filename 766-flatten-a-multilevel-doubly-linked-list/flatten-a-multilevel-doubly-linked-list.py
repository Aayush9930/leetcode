"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child == None:
                curr = curr.next
                continue
            
            child_lst = self.flatten(curr.child)
            curr.child = None
            temp = curr.next
            curr.next = child_lst
            child_lst.prev = curr
            curr2 = child_lst
            while curr2.next:
                curr2 = curr2.next

            if temp:
                curr2.next = temp   
                temp.prev = curr2

            curr = curr.next

        return head
            
            
            




















