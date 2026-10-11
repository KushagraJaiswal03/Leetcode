class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early termination: smallest possible sum is already positive
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
        