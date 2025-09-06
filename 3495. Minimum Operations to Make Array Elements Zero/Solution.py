from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        total_ops = 0

        for left, right in queries:
            weighted_sum = 0    # Accumulates weighted contribution for this query
            level = 0           # Depth level (starts from 0, increases each step)
            block_start = 1     # Left boundary of the current [block_start, block_end] range

            # Iterate over ranges that grow in powers of 4: [1,3], [4,15], [16,63], ...
            while block_start <= right:
                block_end = block_start * 4 - 1

                # Find overlap of [left, right] with [block_start, block_end]
                overlap_start = max(left, block_start)
                overlap_end = min(right, block_end)

                if overlap_start <= overlap_end:
                    # Contribution = number of elements * (level+1)
                    overlap_length = overlap_end - overlap_start + 1
                    weighted_sum += (level + 1) * overlap_length

                # Move to next level
                block_start *= 4
                level += 1

            # Final cost for this query (rounded up division by 2)
            total_ops += (weighted_sum + 1) // 2

        return total_ops



#class Solution:
    #def minOperations(self, queries: List[List[int]]) -> int:
        #res = 0
       # for q in queries:
        #    l = q[0]; r = q[1]; s = 0; op = 0
         #   rage = 1
          #  while rage<=r:
               # sr = max(l, rage)
                #er = min(r, rage*4-1)

               # s += max(0, (op+1)*(er-sr+1))
               # rage *= 4
                # op+=1

           # res += (s+1)//2
       # return res
