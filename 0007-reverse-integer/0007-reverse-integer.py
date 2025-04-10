class Solution:
    def reverse(self, x: int) -> int:
        r = 0

        is_neg = x < 0

        if is_neg:
            x *= -1

        x_str = str(x)

        x_str = x_str[::-1]

        if is_neg:
            r = int(x_str) * -1
        else:
            r = int(x_str)

        if r >= 2 ** 31 or r < -2 ** 31:
            return 0

        return r