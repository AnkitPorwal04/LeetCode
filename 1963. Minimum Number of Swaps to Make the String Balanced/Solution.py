class Solution:
    def minSwaps(self, s: str) -> int:
        max_swap = 0
        closing = 0
        for i in s:
            if i == '[':
                closing -= 1
            else:
                closing += 1
                max_swap = max(max_swap, closing)
        return(max_swap+1)//2
