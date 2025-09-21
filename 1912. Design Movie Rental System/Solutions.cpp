class MovieRentingSystem {
private:
    // For each movie id, store a set of (price, shop).
    // The set is ordered by price ascending, then shop ascending by default.
    unordered_map<int, set<pair<int,int>>> available;

    // Set of currently rented movies. Each element is (price, shop, movie).
    // Tuple compares lexicographically: price, then shop, then movie — exactly the required order.
    set<tuple<int,int,int>> rented;

    // Map (shop, movie) -> price for O(1) lookup of the price for a given shop/movie pair.
    // We pack the two ints into a single 64-bit key.
    unordered_map<long long,int> priceMap;

    // helper to make a unique 64-bit key from (shop, movie)
    static long long makeKey(int shop, int movie) {
        return ( (long long)shop << 32 ) | (unsigned long long)movie;
    }

public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto &e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            available[movie].insert({price, shop});
            priceMap[makeKey(shop, movie)] = price;
        }
    }

    // Return up to 5 shops that have an unrented copy of `movie`,
    // ordered by (price asc, shop asc).
    vector<int> search(int movie) {
        vector<int> ans;
        auto it = available.find(movie);
        if (it == available.end()) return ans;

        int cnt = 0;
        for (auto &pr : it->second) {
            ans.push_back(pr.second);          // pr = {price, shop}
            if (++cnt == 5) break;
        }
        return ans;
    }

    // Rent the movie from the shop: remove from available and add to rented.
    void rent(int shop, int movie) {
        long long k = makeKey(shop, movie);
        int price = priceMap[k];

        // remove from available set for that movie
        auto &s = available[movie];
        s.erase({price, shop});

        // insert into rented set
        rented.insert({price, shop, movie});
    }

    // Drop (return) a previously rented movie: remove from rented and add back to available.
    void drop(int shop, int movie) {
        long long k = makeKey(shop, movie);
        int price = priceMap[k];

        // remove from rented set
        rented.erase({price, shop, movie});

        // add back to available set
        available[movie].insert({price, shop});
    }

    // Report up to 5 cheapest rented movies, each as [shop, movie]
    vector<vector<int>> report() {
        vector<vector<int>> ans;
        int cnt = 0;
        for (const auto &t : rented) {
            if (cnt++ == 5) break;
            int price, shop, movie;
            tie(price, shop, movie) = t;
            ans.push_back({shop, movie});
        }
        return ans;
    }
};
