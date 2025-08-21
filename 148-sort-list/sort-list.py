# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid=slow.next
        slow.next=None
        left_half=self.sortList(head)
        right_half=self.sortList(mid)
        return self.merge(left_half,right_half)

    def merge(self,left_half,right_half):
        dummy=ListNode()
        ans=dummy

        while left_half and right_half:
            if left_half.val > right_half.val:
                ans.next=right_half
                right_half=right_half.next
            else:
                ans.next=left_half
                left_half=left_half.next
            ans=ans.next
        if left_half or right_half:
            ans.next=left_half or right_half
        
        return dummy.next

            
        