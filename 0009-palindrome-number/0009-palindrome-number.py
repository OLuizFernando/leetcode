class Solution:
    def isPalindrome(self, x: int) -> int:
        reversed_x = 0

        temp_x = x
        while temp_x > 0:
            reversed_x *= 10
            reversed_x += temp_x % 10
            temp_x //= 10

        if reversed_x == x:
            return True
        
        return False