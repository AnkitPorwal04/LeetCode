class Solution { 
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();

        // Sort points by:
        // 1. x ascending
        // 2. if x is same → y descending
        sort(points.begin(), points.end(), [](const vector<int>& p1, const vector<int>& p2){
            return p1[0] == p2[0] ? p1[1] > p2[1] : p1[0] < p2[0];
        });

        int count = 0;

        // Fix Alice's position at A
        for(int A = 0; A < n - 1; A++){
            int prev = INT_MIN; // track last valid y (to avoid overcounting)

            // Try Bob's position at B (to the right of A)
            for(int B = A + 1; B < n; B++){
                // Bob must be below Alice (yB ≤ yA) 
                // and higher than any previously counted y (to ensure rectangle is empty)
                if(points[B][1] <= points[A][1] && points[B][1] > prev){
                    count++;              // valid (Alice,Bob) pair
                    prev = points[B][1]; // update last valid y
                }
            }
        }

        return count; // total valid pairs
    }
};
