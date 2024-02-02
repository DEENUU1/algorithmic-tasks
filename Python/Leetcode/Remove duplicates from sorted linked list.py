# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        
        current = head
        prev = None
        duplicates = dict()

        while current:
            if current.val not in duplicates:
                duplicates[current.val] = None
                prev = current
            else:
                prev.next = current.next

            current = current.next
        
        return head
