class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();
        // Sorting the given pairs
        sort(points.begin(), points.end(), [](const vector<int> & p1, const vector<int> & p2)
        {
          /* Sort in such a way that, If the x coordinate of P1 is equal to x-coordinate of P2, then y-coordinate of P1 should be greater than y-coordinate of P2. Otherwise x-coordinate of P1 should be less than x-coordinate of P2.
          */
          return p1[0] == p2[0] ? p1[1] > p2[1] : p1[0]<p2[0];
        });

        int count = 0;
        for(int A=0; A<n-1; A++)
        {  // Iterate over the points
            int prev_bottom_right_y = INT_MIN;
            for(int B = A+1; B<n; B++)
            {   
                // If y-cordinate of Point B is less than equal to y-coordinate of Point A and y-coordinate of Point B is greater than any previous bottom_right coordinate, than increase the counter and update the prev_bottom_right_y.
                if(points[B][1]<=points[A][1] and points[B][1]>prev_bottom_right_y){ count++;
                prev_bottom_right_y = points[B][1];
                }
            }
        }
        return count;
        
    }
};
