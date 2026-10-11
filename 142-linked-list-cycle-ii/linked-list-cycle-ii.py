class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Phase 1: detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # fast reached the end, no cycle

        # Phase 2: find the start of the cycle
        pointer = head
        while pointer != slow:
            pointer = pointer.next
            slow = slow.next

        return pointer