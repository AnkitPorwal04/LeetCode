class Solution {
public:
    int findClosest(int x, int y, int z) {

        // Checking and comparing the distance between the two pair of persons
        // If x is closer to z return 1
        if(abs(z-x)<abs(z-y)) return 1;
        // If y is closer to z return 2
        else if(abs(z-x)>abs(z-y)) return 2;
        // If both x and y arrives at same time, return 0
        else return 0;
        
    }
};
