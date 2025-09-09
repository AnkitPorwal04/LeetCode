class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        m = 10**9 + 7
        # a memoizatio table to store the values of number of people from whom the person can be informed. 
        dp = [0 for i in range (n+1)]
        dp[1] = 1 # the first person will know automatically, so on day 1 there will be one person oin the memory.

        count = 0
        # will will iterate from 2nday to the last day
        for i in range(2, n+1):
            # if the current day-delay is positive i.e. the person can be informed on that day from someone's knowledge
            if i-delay > 0:
                count += dp[i-delay] % m
            # if the current day - foreget is positive, i.e. there might me person who forget the secret and we will remove that
            if i-forget > 0:
                count -= (dp[i-forget] + m) % m
            # update the value of currrent postion in the dp table with the newly calculated count
            dp[i] = count

        # we will return the sum of those people who have strictly remembered the secret.
        # so we will add from n-forget+1 th day till the last day.
        res = sum(dp[n-forget+1 : n+2])%m
        return res
