class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        digits = []
        while n != 0:
            remainder = n % -2

            if remainder == -1:
                remainder = 1
                n = n // -2 + 1
            else:
                n = n // -2
            digits.append(str(remainder))

        digits.reverse()
        return ''.join(digits)