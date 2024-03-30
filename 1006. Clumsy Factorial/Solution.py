class Solution:
    def clumsy(self, n: int) -> int:
        l = []
        itr = 0
        while n > 0:
            l.append(str(n))
            if itr%4 == 0:
                l.append('*')
            elif itr%4 == 1:
                l.append('//')
            elif itr%4 == 2:
                l.append('+')
            elif itr%4 == 3:
                l.append('-')
            itr += 1
            n -= 1
        l.pop()
        l = "".join(l)
        return eval(l)
