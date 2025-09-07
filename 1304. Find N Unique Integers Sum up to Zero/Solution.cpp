class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> ans;

        // Loop through half of n, since we add positive and negative pairs
        for(int i = 0; i < n / 2; i++)
        {
            ans.push_back(i + 1);   // add a positive number
            ans.push_back(-(i + 1)); // add its negative counterpart
        }

        // If n is odd, add 0 to make total count = n
        if(n % 2 != 0)
        {
            ans.push_back(0);
        }

        // Return the constructed vector
        return ans;
    }
};
