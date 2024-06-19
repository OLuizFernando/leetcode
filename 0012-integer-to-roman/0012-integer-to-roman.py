class Solution:
    def intToRoman(self, num: int) -> str:
        units = num % 10
        tens = num // 10 % 10 * 10
        hundreds = num // 100 % 10 * 100
        thousands = num // 1000 % 10 * 1000

        digits = [units, tens, hundreds, thousands]
        roman = ""

        for digit in digits:
            if digit >= 1 and digit <= 9:
                if digit >= 1 and digit <= 3:
                    roman += 'I' * digit
                elif digit == 4:
                    roman += "IV"
                elif digit >= 5 and digit <= 8:
                    roman += "V" + "I" * (digit - 5)
                elif digit == 9:
                    roman += "IX"
            
            elif digit >= 10 and digit <= 90:
                if digit >= 10 and digit <= 30:
                    roman = "X" * (digit // 10) + roman
                elif digit == 40:
                    roman = "XL" + roman
                elif digit >= 50 and digit <= 80:
                    roman = "L" + "X" * (digit // 10 - 5) + roman
                elif digit == 90:
                    roman = "XC" + roman

            elif digit >= 100 and digit <= 900:
                if digit >= 100 and digit <= 300:
                    roman = "C" * (digit // 100) + roman
                elif digit == 400:
                    roman = "CD" + roman
                elif digit >= 500 and digit <= 800:
                    roman = "D" + "C" * (digit // 100 - 5) + roman
                elif digit == 900:
                    roman = "CM" + roman

            elif digit >= 1000 and digit <= 3000:
                roman = "M" * (digit // 1000) + roman

        return roman