class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        v = min(len(v1), len(v2))
        for i in range(v):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v2[i]) > int(v1[i]):
                return -1
        if len(v1) == len(v2):
            return 0
        else:
            if len(v1)>len(v2):
                a = ''.join(v1[len(v2):])
                if int(a) > 0:
                    return 1
                else:
                    return 0
            else:
                a = ''.join(v2[len(v1):])
                if int(a) > 0:
                    return -1
                else:
                    return 0
                
