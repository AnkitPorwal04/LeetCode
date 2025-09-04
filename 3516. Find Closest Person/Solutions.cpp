class Solution {
public:
    int whoReachesFirst(int x, int y, int z) {
        int dist1 = abs(x - z); // distance of Person 1 to Person 3
        int dist2 = abs(y - z); // distance of Person 2 to Person 3

        if (dist1 < dist2) return 1;   // Person 1 closer → arrives first
        else if (dist2 < dist1) return 2; // Person 2 closer → arrives first
        else return 0; // If both are at same distance → arrive together
    }
};
