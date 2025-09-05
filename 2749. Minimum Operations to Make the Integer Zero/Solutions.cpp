class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        // Try all possible k values (number of operations), up to 60
        for (int k = 1; k <= 60; k++) {
            // Remaining value after subtracting k * num2
            long long diff = (long long) num1 - (long long) k * num2;
            if (diff < 0) continue;  // skip invalid (negative) cases

            // Count number of 1-bits in diff (minimum powers of 2 needed)
            int bits = __builtin_popcountll(diff);

            // Valid if diff can be represented with exactly k powers of 2
            if (bits <= k && diff >= k) return k;
        }
        // If no valid k found, return -1
        return -1;
    }
};
