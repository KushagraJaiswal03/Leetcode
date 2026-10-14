class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        
        # no_delete[i]: max sum of subarray ending at i, with no deletion used
        # one_delete[i]: max sum of subarray ending at i, with exactly one deletion used
        no_delete = arr[0]
        one_delete = float('-inf')  # can't delete before any element exists
        max_sum = arr[0]

        for i in range(1, n):
            # Update one_delete BEFORE updating no_delete (uses previous no_delete value)
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(arr[i], no_delete + arr[i])

            max_sum = max(max_sum, no_delete, one_delete)

        return max_sum