# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        l3_head = ListNode()
        l3_curr = l3_head
        plusOne = False

        while (l1_curr or l2_curr):

            digit1 = l1_curr.val if l1_curr else 0
            digit2 = l2_curr.val if l2_curr else 0

            l3_curr.val = digit1 + digit2 + 1 if plusOne else digit1 + digit2

            if l3_curr.val >= 10:
                l3_curr.val -= 10 
                plusOne = True
            else:
                plusOne = False

            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None
            l3_curr.next = ListNode() if l1_curr or l2_curr else None
            l3_curr = l3_curr.next if l1_curr or l2_curr else l3_curr

        if plusOne:
            l3_curr.next = ListNode(val=1)

        return l3_head
        
