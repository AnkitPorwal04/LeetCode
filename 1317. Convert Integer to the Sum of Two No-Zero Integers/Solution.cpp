class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        // intialize x as 1;
        int x = 1;
        vector<int> ans;
        while(true)
        {
            // convert (n-x) and x to string
            string a = to_string(n-x);
            string b = to_string(x);
        // if "0" is present in any index of a or b then we will increment the x and check the other pairs of (x) and (n-x).
            if(a.find("0")!= string::npos || b.find("0")!= string::npos)
            {
                x++;
            }
            // if no 0 is present in both number then we will push_back it in the vector.
            else{
                ans.push_back(x);
                ans.push_back(n-x);
                
                break;

            }
        }
        return ans;
        
    }
};
