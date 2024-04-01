class Solution:
    def simplifyPath(self, path):
        url = []
        path = path.split("/")
        for i in path:
            if url and i == "..":
                url.pop()
            elif i not in [".", "", ".."]:
                url.append(i)
                
        return "/" + "/".join(url)
