class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        s = set()  # people involved in friendships without common language
        for f in friendships:
            d = {}      # record languages known by the first friend
            ok = False  # flag to check if they share any language
            for l in languages[f[0] - 1]:
                d[l] = 1
            for l in languages[f[1] - 1]:
                if l in d:   # found a shared language
                    ok = True
                    break
            if not ok:       # no common language, mark both people
                s.add(f[0] - 1)
                s.add(f[1] - 1)

        m = 0
        c = [0] * (n + 1)  # counts how many in 's' know each language
        for i in s:
            for l in languages[i]:
                c[l] += 1
                m = max(m, c[l])  # track the best language to minimize teaching

        return len(s) - m  # people to teach = total problematic - best overlap
