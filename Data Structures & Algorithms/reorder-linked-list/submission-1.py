# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans = head1 = head
        if head == None or head.next == None:
            return 
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        
        curr = head2
        tmp = head2
        prev = None
        while tmp:
            tmp = tmp.next
            curr.next = prev
            prev = curr
            curr = tmp
        temp1 = head1
        temp2 = prev
        while temp1 and temp2:
            temp1 = temp1.next
            temp2 = temp2.next
            head1.next = prev
            prev.next = temp1
            head1 = temp1 
            prev = temp2
    



          

     
        