class FoodRatings {
    unordered_map<string, pair<string, int>> foodInfo;    // food -> {cuisine, rating}
    unordered_map<string, set<pair<int, string>>> cuisineMap; // cuisine -> set of { -rating, food }

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        int n = foods.size();
        for (int i = 0; i < n; ++i) {
            foodInfo[foods[i]] = {cuisines[i], ratings[i]};
            cuisineMap[cuisines[i]].insert({-ratings[i], foods[i]});
        }
    }
    
    void changeRating(string food, int newRating) {
        auto [cuisine, oldRating] = foodInfo[food];
        // Remove the old (rating, food) pair
        cuisineMap[cuisine].erase({-oldRating, food});
        // Add the new (rating, food) pair
        cuisineMap[cuisine].insert({-newRating, food});
        // Update the stored rating
        foodInfo[food].second = newRating;
    }
    
    string highestRated(string cuisine) {
        // The first element in the set is the highest-rated food (with lexicographical tie-breaker)
        return cuisineMap[cuisine].begin()->second;
    }
};
