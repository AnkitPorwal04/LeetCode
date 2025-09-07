#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> ans; 

        // Add pairs of positive and negative numbers
        for (int i = 0; i < n / 2; i++) {
            ans.push_back(i + 1);    // Add positive number
            ans.push_back(-(i + 1)); // Add corresponding negative number
        }

        // If n is odd, add a 0 to make the count correct
        if (n % 2 != 0) {
            ans.push_back(0);
        }

        return ans;  // Return the resulting array
    }
};
