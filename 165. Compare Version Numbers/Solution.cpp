class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i = 0, j = 0;
        int n = version1.size(), m = version2.size();
        
        while (i < n || j < m) {
            int num1 = 0, num2 = 0;
            
            // take the number until '.' in version1
            while (i < n && version1[i] != '.') {
                num1 = num1 * 10 + (version1[i] - '0');
                i++;
            }
            
            // take the number until '.' in version2
            while (j < m && version2[j] != '.') {
                num2 = num2 * 10 + (version2[j] - '0');
                j++;
            }
            
            // compare this revision
            if (num1 < num2) return -1;
            if (num1 > num2) return 1;
            
            // skip the dot
            i++;
            j++;
        }
        
        return 0;
    }
};
