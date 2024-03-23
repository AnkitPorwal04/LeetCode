class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # counts = []
        # n = list(nums)
        # n.sort()
        # for i in range(len(nums)):
        #     counts.append(n.index(nums[i]))
        #     n.remove(nums[i])
        # return counts
        arr, ans = sorted(nums), []     
        
        for num in nums:
            i = bisect_left(arr,num)    
            ans.append(i)               
            del arr[i]                  
            
        return ans
