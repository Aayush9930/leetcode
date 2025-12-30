# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = defaultdict(int)

        curr = head
        while curr:
            f[curr.val] += 1
            curr = curr.next
        
        remove_set = set()

        for key in f:
            if f[key] > 1:
                remove_set.add(key)
        
        prev = None
        curr = head

        while curr:
            if curr.val in remove_set and prev == None:
                while curr and curr.val in remove_set:
                    head = head.next
                    curr = curr.next
            elif curr.val in remove_set:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head  