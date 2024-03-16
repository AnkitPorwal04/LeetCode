class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if nums.count(i)>len(nums)/3:
                s.add(i)
        return list(s)
