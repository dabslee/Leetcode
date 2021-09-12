# Complexity O(nk) where k is the number of lists and n is
# number of elements in all lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        head = prev = None
        lists = list([lst for lst in lists if lst != None])
        while lists:
            # get the list with the smallest curr val
            smallest = ListNode(val=10**4)
            smallest_i = 0
            for i, lst in enumerate(lists):
                if lst.val < smallest.val:
                    smallest = lst
                    smallest_i = i
            # add it to the ongoing list
            if head == None:
                head = prev = smallest
            else:
                prev.next = smallest
                prev = smallest
            # increment on the chosen list
            lists[smallest_i] = smallest.next
            
            # remove empty lists
            lists = list([lst for lst in lists if lst != None])
        return head

class LinkedList(ListNode):
    def __init__(self, lst):
        if not lst:
            self = None
            return
        ListNode.__init__(self)
        curr = self
        curr.val = lst[0]
        for i in lst[1:]:
            curr.next = ListNode(val=i)
            curr = curr.next
    def asList(self):
        curr = self
        retval = [curr.val]
        while curr.next:
            curr = curr.next
            retval.append(curr.val)
        return retval
    def __str__(self):
        return str(self.asList())

sol = Solution()
inp = [[1,4,5],[1,3,4],[2,6]]
print(sol.mergeKLists(
    list([LinkedList(lst) for lst in inp])
))