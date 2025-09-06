class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        long long result = 0;

        // Go through each query range [l, r]
        for (auto q : queries) {
            long long l = q[0];
            long long r = q[1];
            long long sum = 0;
            long long operation = 0;

            // Break the range into chunks of size growing by powers of 4
            for (long long range = 1; range <= r; range *= 4) {
                // Find the actual start (sr) and end (er) of the overlap with [l, r]
                long long sr = max(l, range);
                long long er = min(r, range * 4 - 1);

                // Add contribution of this chunk, multiplied by current operation count
                sum += max(0ll, ++operation * (er - sr + 1));
            }

            // Add half of the total sum (rounded up) to result
            result += (sum + 1) / 2;
        }

        // Return the final total operations across all queries
        return result;
    }
};
