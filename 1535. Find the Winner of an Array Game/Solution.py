class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if n <= k:
            return max(arr)
        count = 0
        winner = arr[0]
        for x in arr[1:]:
            if x > winner:
                winner = x
                count = 1
            else:
                count += 1
            if count == k:
                break        
        return winner
