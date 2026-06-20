# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        prev = head
        curr = head
        while curr:
            curr = curr.next
            prev.next = temp
            temp = prev
            prev = curr
        return temp


            

        