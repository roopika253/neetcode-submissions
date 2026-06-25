# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        s = 0
        ans = temp = ListNode()
        while l1 or l2:
            s1 = l1.val if l1 else 0
            s2 = l2.val if l2 else 0
            s = s1 + s2 + carry
            curr_sum = s%10
            temp.next = ListNode(curr_sum)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            carry = s // 10
           
        if carry :
            temp.next = ListNode(carry)
        return ans.next

        

        