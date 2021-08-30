# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        currnode = l1
        digit = 0
        while currnode != None:
            num1 += currnode.val * 10**(digit)
            digit += 1
            currnode = currnode.next

        num2 = 0
        currnode = l2
        digit = 0
        while currnode != None:
            num2 += currnode.val * 10**(digit)
            digit += 1
            currnode = currnode.next

        print(f"{num1} + {num2}")

        answernum = num1 + num2
        answerlist = ListNode()
        currnode = answerlist
        while True:
            currnode.val = answernum % 10
            answernum = answernum // 10
            if answernum == 0:
                break
            currnode.next = ListNode()
            currnode = currnode.next
        return answerlist