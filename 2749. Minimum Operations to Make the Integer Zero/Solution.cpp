class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        // Try values of k from 0 to 59 (sufficient range since diff shrinks fast)
        for (int k = 0; k < 60; k++) {
            
            // Calculate the remaining value after subtracting k * num2
            long long diff = (long long)num1 - (long long)k * num2;
            
            // If diff becomes negative, this k is invalid, skip it
            if (diff < 0) {
                continue;
            }

            // Count how many bits are set to 1 in the binary representation of diff
            int bits = __builtin_popcountll(diff);

            // Valid case if:
            // 1. The number of 1-bits (bits) is <= k
            //    → because we can "distribute" these bits across k terms
            // 2. diff >= k
            //    → ensures there are enough units to form k terms
            if (bits <= k && diff >= k) {
                return k;  // Found the minimum k that works
            }
        }
        
        // If no valid k is found, return -1
        return -1;
    }
};
