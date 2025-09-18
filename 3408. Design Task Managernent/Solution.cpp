class TaskManager {
    using pii = pair<int,int>;
    priority_queue<pii> maxheap;
    unordered_map<int,pii> tid_priority_uid;
public:
    TaskManager(vector<vector<int>>& tasks) {
        for(auto& task: tasks){
            maxheap.push({task[2],task[1]});
            tid_priority_uid[task[1]] = {task[2],task[0]};
        }
    }
    
    void add(int userId, int taskId, int priority) {
        maxheap.push({priority,taskId});
        tid_priority_uid[taskId] = {priority,userId};
    }
    
    void edit(int taskId, int newPriority) {
        maxheap.push({newPriority,taskId});
        tid_priority_uid[taskId].first = newPriority;
    }
    
    void rmv(int taskId) {
        tid_priority_uid.erase(taskId);
    }
    
    int execTop() {
        while(!maxheap.empty()){
            pii curr = maxheap.top();
            maxheap.pop();

            if(tid_priority_uid.count(curr.second) and tid_priority_uid[curr.second].first==curr.first){
                int taskId = tid_priority_uid[curr.second].second;
                tid_priority_uid.erase(curr.second);
                return taskId;
            }
        }
        return -1;
    }
};
