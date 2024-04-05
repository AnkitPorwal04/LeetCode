class Solution:
    def makeGood(self, s: str) -> str:
        l = [
            "Aa",
            "aA",
            "Bb",
            "bB",
            "Cc",
            "cC",
            "Dd",
            "dD",
            "Ee",
            "eE",
            "Ff",
            "fF",
            "Gg",
            "gG",
            "Hh",
            "hH",
            "Ii",
            "iI",
            "Jj",
            "jJ",
            "Kk",
            "kK",
            "Ll",
            "lL",
            "Mm",
            "mM",
            "Nn",
            "nN",
            "Oo",
            "oO",
            "Pp",
            "pP",
            "Qq",
            "qQ",
            "Rr",
            "rR",
            "Ss",
            "sS",
            "Tt",
            "tT",
            "Uu",
            "uU",
            "Vv",
            "vV",
            "Ww",
            "wW",
            "Xx",
            "xX",
            "Yy",
            "yY",
            "Zz",
            "zZ",
        ]
        flag = True
        while flag:
            for i in l:
                if i in s:
                    s = s.replace(i, '')
                    break
            else:
                flag = False
        return s
