class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        need = [0] * 26
        window = [0] * 26

        for char in p:
            need[ord(char) - ord('a')] += 1

        for i in range(len_p):
            window[ord(s[i]) - ord('a')] += 1

        result = []
        if window == need:
            result.append(0)

        for right in range(len_p, len_s):
            window[ord(s[right]) - ord('a')] += 1
            left_char = s[right - len_p]
            window[ord(left_char) - ord('a')] -= 1

            if window == need:
                result.append(right - len_p + 1)

        return result