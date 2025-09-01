class Solution {
    #define pdi pair<double, int>
    void heapPush(priority_queue<pdi>& maxheap, vector<vector<int>>& classes, int i){
        double curr_avg= (double)classes[i][0]/classes[i][1];
        double new_avg= ((double) classes[i][0]+1)/(classes[i][1]+1);
        double possible_inc= new_avg - curr_avg;
        maxheap.push(make_pair(possible_inc, i));
    }
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        int n=classes.size();
        priority_queue<pdi> maxheap;
        for(int i=0; i<n; i++){
            heapPush(maxheap, classes, i);
        }
        while(extraStudents--){
            pdi curr= maxheap.top();
            maxheap.pop();
            int idx = curr.second;
            classes[idx][0]++;
            classes[idx][1]++;
            heapPush(maxheap, classes, idx);
        }
        double final_avg=0.0;
        for(int i=0; i<n; i++){
            final_avg+= (double) classes[i][0]/classes[i][1];
        }
        return final_avg/n;
    }
};
