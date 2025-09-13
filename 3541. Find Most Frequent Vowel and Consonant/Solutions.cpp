class Solution {
public:
    int maxFreqSum(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u'};
        unordered_map<char,int> dicv, dicc;
        // count frequencies
        for(char c : s) {
            if(vowels.count(c)) {
                dicv[c]++;
            } else {
                dicc[c]++;
            }
        }
        // find maximum frequencies
        int maxVowel = 0, maxConsonant = 0;
        for(auto &p : dicv) {
            maxVowel = max(maxVowel, p.second);
        }
        for(auto &p : dicc) {
            maxConsonant = max(maxConsonant, p.second);
        }
        return maxVowel + maxConsonant;
    }
};
