class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -2  # default: already sorted (right - left + 1 = 0)

        max_seen = float('-inf')
        min_seen = float('inf')

        # Left-to-right pass: track the max so far, find the last index
        # where a number is smaller than that max (out of order on the right side)
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        # Right-to-left pass: track the min so far, find the first index
        # (smallest index) where a number is greater than that min
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right - left + 1