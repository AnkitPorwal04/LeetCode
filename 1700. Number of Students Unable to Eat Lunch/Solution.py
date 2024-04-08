class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1

        for i in range(len(sandwiches)):
            if count[sandwiches[i]] == 0:
                return len(sandwiches) - i
            count[sandwiches[i]] -= 1

        return 0
