class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answernum = 0

        currnode = l1
        digit = 0
        while currnode != None:
            answernum += currnode.val * 10**(digit)
            digit += 1
            currnode = currnode.next

        currnode = l2
        digit = 0
        while currnode != None:
            answernum += currnode.val * 10**(digit)
            digit += 1
            currnode = currnode.next

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