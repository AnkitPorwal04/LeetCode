class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0          # store total sum
        nums = []        # store absolute values
        count = 0        # count negative numbers

        for i in matrix:
            for j in i:
                if j <= 0:
                    nums.append(-j)   # add absolute value
                    res -= j          # add absolute value to sum
                    count += 1        # increase negative count
                else:
                    nums.append(j)    # add value
                    res += j          # add value to sum

        if count % 2 != 0:
            nums.sort()               # find smallest absolute value
            res -= (nums[0] * 2)      # make one number negative

        return res
