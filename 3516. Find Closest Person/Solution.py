class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
      # if distance between x and z is lower then return 1 else 2.
      # we will use abs to calculate absolute difference, 
        if abs(z-x) < abs(z-y):
            return 1
        elif abs(z-x) > abs(z-y):
            return 2
        else:
            return 0
