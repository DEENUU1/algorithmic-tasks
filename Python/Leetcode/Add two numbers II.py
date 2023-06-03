class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1, st2 = [], []

        while l1:
            st1.append(l1.val)
            l1 = l1.next
        while l2:
            st2.append(l2.val)
            l2 = l2.next

        nextNode, remainder = None, 0
        while st1 or st2 or remainder:
            v1 = st1.pop() if st1 else 0
            v2 = st2.pop() if st2 else 0
            remainder, val = divmod(v1 + v2 + remainder, 10)
            node = ListNode(val, nextNode)
            nextNode = node
        
        return node