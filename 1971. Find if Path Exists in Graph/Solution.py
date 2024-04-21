class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        # Beats 100% by this code 🚀
        if [source, destination] in edges:
            return True

        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        des_list = [graph[source]]
        visits = [False] * n
        while des_list:
            new_list = []
            for des in des_list:
                if destination in des:
                    return True
                for node in des:
                    if visits[node]:
                        continue
                    visits[node] = True
                    new_list.append(graph[node])
            des_list = new_list

        return False
