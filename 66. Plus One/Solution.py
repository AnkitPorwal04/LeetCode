class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(i) for i in digits)
        new_s = str(int(s)+1)
        ans = []
        for i in new_s:
            ans.append(int(i))
        return ans
