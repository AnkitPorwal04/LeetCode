class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        long long mod = 1000000007;
        vector<long long> dp(n+1, 0);
        dp[1] = 1;
        for(int day=1; day<=n; day++){
            long long people = dp[day];
            if(people == 0) continue;
            
            int start = day + delay;
            int end = day + forget -1;
            for(int i= start; i<=end && i<=n; i++){
                dp[i] = (dp[i] + people)% mod;
            }
        }
        long long result=0;
        for(int day= n-forget+1; day<=n; day++){
            if(day>=1){
              result=(result + dp[day])% mod;
            }
        }
        return (int) result;
    }
};
