from sortedcontainers import SortedSet # f.or better time complexity
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.map1 = defaultdict(SortedSet)  # cuisine -> (rating, food)
        self.map2 = defaultdict(list)  # food -> (cuisine, rating)
        for x, y, z in zip(foods, cuisines, ratings):
            self.map1[y].add((-z, x))
            self.map2[x].append((y, z))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.map2[food][0]
        self.map1[cuisine].remove((-rating, food))
        self.map1[cuisine].add((-newRating, food))
        self.map2[food][0] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.map1[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
