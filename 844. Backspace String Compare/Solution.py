class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns = []
        nt = []
        for i in range(len(s)):
            if s[i]=='#':
                if ns:
                    ns.pop()
            else:
                ns.append(s[i])
        for i in range(len(t)):
            if t[i]=="#":
                if nt:
                    nt.pop()
            else:
                nt.append(t[i])
        if ns == nt:
            return True
        else:
            return False
