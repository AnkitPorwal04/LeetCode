class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
    def get(self, key: int) -> int:
        a = self.dic.get(key, -1)
        if a != -1:
            self.dic.pop(key)
            self.dic[key] = a
        return a

    def put(self, key: int, value: int) -> None:
        if key in self.dic.keys():
            self.dic.pop(key)
            self.dic[key] = value
        else:
            self.dic[key] = value
            if len(self.dic)>self.capacity:
                k = list(self.dic.keys())[0]
                del self.dic[k]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
