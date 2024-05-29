class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        reversed_s = s[::-1]
        decimal = 0
        for i, bit in enumerate(reversed_s):
            if bit == '1':
                decimal += 2**i
        while decimal != 1:
            if decimal % 2 == 0:
                decimal //= 2
                steps += 1
            else:
                decimal += 1
                steps += 1
        return steps
