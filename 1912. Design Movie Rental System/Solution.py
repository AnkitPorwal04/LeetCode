class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}  # (shop, movie) -> price
        self.movie_shops = {}  # movie -> list of (price, shop)
        self.rented = set()  # (shop, movie) that are currently rented

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        # Sort shops by price for each movie initially
        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]
