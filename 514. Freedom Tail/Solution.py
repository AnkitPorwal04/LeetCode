class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    @functools.lru_cache(None)
    def dfs(ring: str, index: int) -> int:
      if index == len(key):
        return 0
      ans = math.inf
      for i, r in enumerate(ring):
        if r == key[index]:
          minRotates = min(i, len(ring) - i)
          newRing = ring[i:] + ring[:i]
          remainingRotates = dfs(newRing, index + 1)
          ans = min(ans, minRotates + remainingRotates)

      return ans

    return dfs(ring, 0) + len(key)
