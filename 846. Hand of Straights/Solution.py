class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        itrs = n//groupSize
        hand.sort()
        for i in range(itrs):
            group = []
            for j in range(groupSize):
                if j == 0:
                    group.append(hand.pop(0))
                else:
                    num = group[-1]+1
                    if num in hand:
                        hand.remove(num)
                        group.append(num)
                    else:
                        return False
        return True
