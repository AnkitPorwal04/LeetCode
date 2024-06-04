class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l,r = 0,1
        while len(intervals)>1 and r<len(intervals):
            if intervals[l][-1] >= intervals[r][0]:
                intervals.insert(r+1,[intervals[l][0], max(intervals[r][-1],intervals[l][-1])])
                intervals.pop(r)
                intervals.pop(l)
            else:
                l += 1
                r += 1
        return intervals
