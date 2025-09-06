#include <vector>
#include <algorithm>  
using namespace std;

class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        long long result = 0;  // final answer across all queries

        // Iterate through each query [l, r]
        for (auto& q : queries) {
            long long l = q[0];     // left bound of query
            long long r = q[1];     // right bound of query
            long long sum = 0;      // accumulate weighted contribution
            long long operations = 0; // counts how many "segments" processed

            // Divide the range into blocks of size powers of 4
            for (long long range = 1; range <= r; range *= 4) {
                // sr = start of the current block, clipped to >= l
                long long sr = max(range, l);

                // er = end of the current block, clipped to <= r
                long long er = min(r, range * 4 - 1);

                // Increment operations (which block we are on)
                // Multiply by number of elements in this segment
                // If sr > er, contribution is 0
                sum += max(0LL, ++operations * (er - sr + 1));
            }

            // Each query's contribution is (sum + 1) / 2
            // (equivalent to ceiling division by 2)
            result += (sum + 1) / 2;
        }

        // Return total result across all queries
        return result;
    }
};
