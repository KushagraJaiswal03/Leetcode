# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes remaining from `head`
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1

        if count < k:
            return head  # fewer than k nodes left, leave as-is

        # Reverse the first k nodes
        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # `head` is now the tail of this reversed group;
        # recursively reverse the rest, and attach it
        head.next = self.reverseKGroup(current, k)

        return prev  # new head of this reversed group
        