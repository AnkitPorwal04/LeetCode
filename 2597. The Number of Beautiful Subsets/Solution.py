class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # nums = [2,4,6]
        # k = 2
        # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # [2], [4], [6], [2, 6] -> 4 ans
        # SOLUTION
        # num - k or n + k

        count = 0
        lenNums = len(nums)

        def explore(index):
            nonlocal count
            if lenNums == index:
                count += 1
                return

            num = nums[index]

            if num - k not in visited and num + k not in visited:
                visited[num] += 1
                explore(index + 1)
                visited[num] -= 1
                if visited[num] == 0:
                    del visited[num]

            explore(index + 1)

        visited = defaultdict(int)
        explore(0)
        return count - 1
