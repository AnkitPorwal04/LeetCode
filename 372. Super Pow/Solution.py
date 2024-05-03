class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        intb = 0
        for i in b:
            intb = intb*10 + i

        return pow(a,intb,1337)
