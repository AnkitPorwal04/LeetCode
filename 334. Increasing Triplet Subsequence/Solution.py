class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one, two = inf, inf
        for i in nums:
            if one >= i:
                one = i
            elif two >= i:
                two = i
            else:
                return True
        return False

