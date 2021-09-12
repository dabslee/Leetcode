# Complexity O(n lg n) where n is number of elements in all lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        # parse and append all lists
        full_list = []
        for i in range(len(lists)):
            if lists[i] == None:
                continue
            full_list.append(lists[i].val)
            curr = lists[i]
            while curr.next:
                curr = curr.next
                full_list.append(curr.val)
        if len(full_list) == 0:
            return None

        # sort appended list
        full_list.sort()

        # create and return linked-list
        curr = head = ListNode(val=full_list[0])
        for i in full_list[1:]:
            curr.next = ListNode()
            curr = curr.next
            curr.val = i
        return head