class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0 #length tracking variable
        res = 0 #final result
        for i in nums:
            if i == 0: #we will find for a number to be 0
                l += 1 #we will check how many continuous zeros we have located (using length variable)
                res += l # we will add length of zeros to res (why?)
              # count:     1, 2, 3, 4
              # Subarrays: 1, 3, 6, 10
          #                  +2,+3,+4...... (#length of subarray we will form)
            else:
                l = 0 # getting our length back to zero because sub array was broken.
        return res
