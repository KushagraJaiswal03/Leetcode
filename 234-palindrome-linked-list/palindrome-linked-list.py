class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: find the middle of the list using slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: compare the first half and the reversed second half
        left, right = head, prev
        is_palin = True
        while right:  # right (reversed half) is the shorter or equal half
            if left.val != right.val:
                is_palin = False
                break
            left = left.next
            right = right.next

        return is_palin