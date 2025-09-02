class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();

        // Sort points:
        // 1. By x ascending
        // 2. If x is same, then by y descending
        sort(points.begin(), points.end(), [](const vector<int>& p1, const vector<int>& p2){
            return p1[0] == p2[0] ? p1[1] > p2[1] : p1[0] < p2[0];
        });

        int count = 0;

        // Fix one point A
        for(int A = 0; A < n - 1; A++){
            int prev = INT_MIN; // Tracks the maximum y seen so far (to avoid duplicate counting)

            // Compare with every next point B
            for(int B = A + 1; B < n; B++){
                // Condition: B should be below or at same height as A (yB ≤ yA),
                // but also strictly greater than the previously counted y
                if(points[B][1] <= points[A][1] && points[B][1] > prev){
                    count++;              // Valid pair found
                    prev = points[B][1]; // Update prev to avoid overcounting
                }
            }
        }

        return count;
    }
};
