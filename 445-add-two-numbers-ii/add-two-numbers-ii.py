# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        curr = l1
        while curr:
            stk1.append(curr.val)
            curr = curr.next
        stk2 = []
        curr = l2
        while curr:
            stk2.append(curr.val)
            curr = curr.next
        
        carry = 0
        curr = None
        while stk1 and stk2:
            total = stk1.pop() + stk2.pop() + carry
            if total > 9:
                carry = 1
                new_node = ListNode(total - 10)
            elif total <= 9:
                new_node = ListNode(total)
                carry = 0

            if curr == None:
                curr = new_node
                continue
            new_node.next = curr
            curr = new_node

        while stk1:
            total = stk1.pop() + carry
            if total > 9:
                carry = 1
                new_node = ListNode(total - 10)
            elif total <= 9:
                new_node = ListNode(total)
                carry = 0
            if curr == None:
                curr = new_node
                continue
            new_node.next = curr
            curr = new_node
    
        while stk2:
            total = stk2.pop() + carry
            if total > 9:
                carry = 1
                new_node = ListNode(total - 10)
            elif total <= 9:
                new_node = ListNode(total)
                carry = 0
            if curr == None:
                curr = new_node
                continue
            new_node.next = curr
            curr = new_node
    
        if carry == 1:
            new_node = ListNode(1)
            new_node.next = curr
            curr = new_node
        
        return curr
