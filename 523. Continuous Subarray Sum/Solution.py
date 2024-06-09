class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s, prev_d, set_d = 0, 0, set()
        for num in nums:
            s += num
            d = s%k
            if d in set_d:
                return True
            set_d.add(prev_d)
            prev_d = d
        return False    
