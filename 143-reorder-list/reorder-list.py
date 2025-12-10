# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # finding the mid
        s, f = head, head
        while f and f.next:
            s = s.next 
            f = f.next.next 
        
        # reversing the second half 
        
        curr = s.next
        s.next = None
        prev = None 

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp

        # now prev has the head of the reversed list
        dummy = node = ListNode()

        x, y = head, prev

        while x and y:
            node.next = x
            x = x.next
            node = node.next
            node.next = y
            y = y.next
            node = node.next
        if x:
            node.next = x
        if y:
            node.next = y
        
        return dummy.next


        


        

        