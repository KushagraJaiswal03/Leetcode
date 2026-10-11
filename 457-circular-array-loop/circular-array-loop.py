class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0

            while True:
                slow = next_index(slow)
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                fast = next_index(fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                fast = next_index(fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                if slow == fast:
                    # Check for a cycle of length 1 (self-loop), which doesn't count
                    if slow == next_index(slow):
                        break
                    return True

            # Mark all nodes visited in this failed attempt as 0 (dead ends)
            # to avoid re-processing them and to break any direction mismatch chains
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                next_j = next_index(j)
                nums[j] = 0
                j = next_j

        return False
        