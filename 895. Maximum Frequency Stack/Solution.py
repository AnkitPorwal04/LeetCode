class FreqStack:

    def __init__(self):
        self.stack = {}
        self.cnt = {}
        self.maxCnt = 0    

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stack[valCnt] = []
        self.stack[valCnt].append(val)


    def pop(self) -> int:
        res = self.stack[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.maxCnt]:
            self.maxCnt -= 1
        return res
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
