# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1 if l1.val < l2.val else l2
        curr1 = l1
        curr2 = l2
        prev = None

        while curr1 and curr2:
            if curr1.val < curr2.val:
                if prev:
                    prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                if prev:
                    prev.next = curr2
                prev = curr2
                curr2 = curr2.next

        if curr1:
            prev.next = curr1
        elif curr2:
            prev.next = curr2

        return head