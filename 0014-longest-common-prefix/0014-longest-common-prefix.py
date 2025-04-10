class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        max_len = 0

        for s in strs:
            if len(s) > max_len:
                max_len = len(s)

        for _ in range(max_len):
            for s in strs:
                if s[:len(common_prefix)] != common_prefix:
                    common_prefix = common_prefix[:-1]

        return common_prefix