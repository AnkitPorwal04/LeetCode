class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        O(N lg N) solution requires using a dequee to manage open straight hands rather than returning the pointer to each next number each time.
        """

        hand.sort()

        dq = collections.deque([])

        #print(card_ct)
        for card in hand:
            #print(card)
            if len(dq) >0:
                if dq[-1][1] == card -1:
                    item = dq.pop()
                    item[0] += 1
                    item[1] = card
                elif dq[-1][1] == card:
                    item = [1,card]
                else:
                    return False # in this case there will not be anything to fill the open straight
            else:
                item = [1,card]
        
            if item[0] < groupSize:
                dq.appendleft(item) # move it to left so we can deal with new new ones 

        
            
                    

        return len(dq) == 0
