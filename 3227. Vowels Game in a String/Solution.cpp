class Solution {
public:
    bool doesAliceWin(string s) {
        int flag = true;
        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == 'a' || s[i] == 'e'|| s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
            {
                return flag;
            }
        }
        return false;

        
    }
};
