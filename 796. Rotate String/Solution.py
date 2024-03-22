class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # l = len(s)
        # s = list(s)
        # while l:
        #     a = s.pop(0)
        #     s.append(a)
        #     if s == list(goal):
        #         return True
        #     l = l -1 
        # return False

        if len(s) == len(goal):
            if s in goal + goal:
                return True
        
        
