class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = []
        dest = []
        for i in paths:
            source.append(i[0])
            dest.append(i[1])
        for i in dest:
            if i not in source:
                return i
