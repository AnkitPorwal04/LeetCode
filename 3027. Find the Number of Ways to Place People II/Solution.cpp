class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        int n = points.size();
        //Sorting the pairs, if x-coordinate of Point A and Point B is equal, then y-coordinate then y-coordinate of Point A should be greater than Point B otherwise x-coordinate of POint A is less than Point B.
        sort(points.begin(), points.end(), [](const vector<int> &P1, const vector<int> &P2)
        {
            return P1[0] == P2[0] ? P1[1] > P2[1] : P1[0] < P2[0];
        });

        int count = 0;
        for(int a = 0; a<n-1; a++)
        {
            // initialize a bottom_right
            int prev_bottom_right_y = INT_MIN;
            for(int b = a+1; b<n; b++)
            {
                // Increase count if y-coordinate of Point B is less than equal to y-coordinate of Point A and y-coordinate of Point B is greater than the prev stored bottom right.
                if(points[b][1]<=points[a][1] and points[b][1]>prev_bottom_right_y)
                {
                    count++;
                    prev_bottom_right_y = points[b][1];
                }
            }
        }
        return count;
        
    }
};
