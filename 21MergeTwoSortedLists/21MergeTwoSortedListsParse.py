# Complexity O(n lg n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get list 1
        lst1 = []
        if l1 != None:
            lst1 = [l1.val]
            while l1.next:
                l1 = l1.next
                lst1.append(l1.val)

        # get list 2
        lst2 = []
        if l2 != None:
            lst2 = [l2.val]
            while l2.next:
                l2 = l2.next
                lst2.append(l2.val)
        
        # merge and sort
        lst = sorted(lst1+lst2)
        if len(lst) == 0:
            return None

        # return result as linked list
        head = ListNode(val=lst[0])
        curr = head
        for i in range(1,len(lst)):
            curr.next = ListNode(val=lst[i])
            curr = curr.next
        return head