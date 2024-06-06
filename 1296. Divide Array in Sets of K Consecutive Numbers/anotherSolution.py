class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        itrs = n//k
        nums.sort()
        for i in range(itrs):
            group = []
            for j in range(k):
                if j == 0:
                    group.append(nums.pop(0))
                else:
                    num = group[-1]+1
                    if num in nums:
                        nums.remove(num)
                        group.append(num)
                    else:
                        return False
        return True
