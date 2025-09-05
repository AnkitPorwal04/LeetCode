class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    # We will check for all the possible values of k till 60  
        for k in range(60):
        # We will calculate the difference and check it's bit count. 
            diff = num1 - k * num2
            #if diff is greater than zero then only we will continue
            if diff<0:
                continue
            
            bits = diff.bit_count()
            # bits should be lesser than the number of operations and operations should be less than k.          
            if bits<=k and diff>=k:
                return k
        return -1
