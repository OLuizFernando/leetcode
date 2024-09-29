class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        left = 0
        longest_substr_len = 0

        for char in s:
            for i in range(left, len(s)):
                if s[i] not in substr:
                    substr.append(s[i])
                else:
                    substr.clear()
                    left += 1
                    break

                if len(substr) > longest_substr_len:
                    longest_substr_len = len(substr)

        return longest_substr_len