class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        all_even = 0
        all_odd = 0
        odd_even = 0
        even_odd = 0

        for i in nums:
            if i%2 == 0:
                all_even += 1
            else:
                all_odd += 1

        for i in nums:
            if odd_even % 2 == 0:
                if i % 2 == 1:
                    odd_even += 1
            else:
                if i % 2 == 0:
                    odd_even += 1

            if even_odd % 2 == 0:
                if i % 2 == 0:
                    even_odd += 1
            else:
                if i % 2 == 1:
                    even_odd += 1

        return(max(all_even, all_odd, odd_even, even_odd))
