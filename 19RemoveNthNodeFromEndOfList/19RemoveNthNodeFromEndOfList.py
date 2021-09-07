# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # read in the list
        curr = head
        lst = [curr]
        while curr.next:
            curr = curr.next
            lst.append(curr)

        # check for only one element list
        if len(lst) == 1:
            return None

        # remove element nth from end of list
        curr = lst[len(lst) - n]
        if len(lst) - n == 0: # remove first element
            return curr.next
        prev = lst[len(lst) - n - 1]
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None
        return head