class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        ans = 0
        for i in range(n):
            ans += abs(students[i]-seats[i])
        return ans
