class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        need = [0] * 26
        window = [0] * 26

        for char in s1:
            need[ord(char) - ord('a')] += 1

        for i in range(len1):
            window[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        for right in range(len1, len2):
            window[ord(s2[right]) - ord('a')] += 1
            left_char = s2[right - len1]
            window[ord(left_char) - ord('a')] -= 1

            if window == need:
                return True

        return False
        