# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x, y = l1, l2
        carry = 0

        dummy = node = ListNode()

        while x and y:
            total = x.val + y.val + carry
            if total > 9:
                carry = 1
                node.next = ListNode(total - 10)
                node = node.next
            
            else:
                carry = 0
                node.next = ListNode(total)
                node = node.next
            
            x = x.next
            y = y.next
        
        while x:
            total = carry + x.val
            if total > 9:
                carry = 1
                node.next = ListNode(total - 10)
                node = node.next
            else:
                carry = 0
                node.next = ListNode(total)
                node = node.next
            
            x = x.next
        
        while y:
            total = carry + y.val
            if total > 9:
                carry = 1
                node.next = ListNode(total - 10)
                node = node.next
            else:
                carry = 0
                node.next = ListNode(total)
                node = node.next
            
            y = y.next

        if carry:
            node.next = ListNode(carry)
        
        return dummy.next