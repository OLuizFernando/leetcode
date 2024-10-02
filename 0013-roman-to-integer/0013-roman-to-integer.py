class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        subtracts = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }

        res = 0

        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1 or s[i] not in ["I", "X", "C"]:
                res += symbols[s[i]]
                continue

            if s[i] in ["I", "X", "C"] and s[i + 1] in subtracts[s[i]]:
                res -= symbols[s[i]]
                continue

            res += symbols[s[i]]

        return res
        