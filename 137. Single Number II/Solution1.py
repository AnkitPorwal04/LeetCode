class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {num: 0 for num in nums}
        for num in nums:
            hash_map[num] += 1
        for key, value in hash_map.items():
            if value == 1:
                return key
