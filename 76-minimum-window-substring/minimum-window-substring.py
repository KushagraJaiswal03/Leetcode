class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        required = len(need)  # number of distinct chars in t that must be fully satisfied
        formed = 0  # number of distinct chars currently satisfied in the window

        window_count = {}
        left = 0
        best_len = float('inf')
        best_left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in need and window_count[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in need and window_count[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_left:best_left + best_len]