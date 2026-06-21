# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point = head
        length = 0
        while point:
            length += 1
            point = point.next
        if length == 1:
            return None
        remove_index = length - n + 1
        if remove_index == 1:
            return head.next
       
        point = head
        prev = None
        for i in range(remove_index-1):
            prev = point
            point = point.next
        if prev:
            prev.next = point.next
        return head

        