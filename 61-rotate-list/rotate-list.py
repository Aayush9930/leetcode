# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        tail = curr
        tail.next = head
        k = k % count
        reach = count - k
        
        curr = head
        count = 0
        while count != reach - 1:
            count += 1
            curr = curr.next
        head = curr.next
        curr.next = None

        return head


        
