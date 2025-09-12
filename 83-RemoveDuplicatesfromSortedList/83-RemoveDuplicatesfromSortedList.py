# Last updated: 9/12/2025, 8:32:24 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        root=head

        while root and root.next:
            if root.val==root.next.val:
                root.next=root.next.next
            else: 
                root=root.next
        return head
        