class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        vector<int> ans;
        
        int x = 1;  // Start checking from x = 1
        
        while (true) {
            // Convert (n - x) and x into strings for zero digit check
            string a = to_string(n - x);
            string b = to_string(x);
            
            // Check if either a or b contains the digit '0'
            if (a.find('0') != string::npos || b.find('0') != string::npos) {
                x++;  // If either contains '0', increment x and continue
            } else {
                // If both numbers do NOT contain '0', we found the pair
                ans.push_back(n - x);  // Add first integer
                ans.push_back(x);      // Add second integer
                break;                 // Exit the loop
            }
        }
        
        return ans;  // Return the result vector
    }
};
