class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        long long mod = 1000000007;
        // dp[i] will store how many people learn the secret on day i
        vector<long long> dp(n+1, 0);
        dp[1] = 1;  // on day 1, exactly one person knows the secret

        // Go day by day to see how the secret spreads
        for(int day = 1; day <= n; day++) {
            long long people = dp[day];  // number of people who learn the secret on this day
            if(people == 0) continue;    // if no one learns today, skip

            // A person can start sharing only after "delay" days
            int start = day + delay;
            // A person will forget the secret after "forget" days, so last day they can share is (forget - 1) after learning
            int end = day + forget - 1;

            // Spread the secret to each valid day in this range
            for(int i = start; i <= end && i <= n; i++) {
                dp[i] = (dp[i] + people) % mod;
            }
        }

        // Count how many people still remember the secret on the nth day
        long long result = 0;
        for(int day = n - forget + 1; day <= n; day++) {
            if(day >= 1) {
                result = (result + dp[day]) % mod;
            }
        }
        return (int) result;
    }
};
