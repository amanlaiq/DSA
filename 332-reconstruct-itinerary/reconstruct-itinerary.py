class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for src, dest in tickets:
            graph[src].append(dest)
        for airport in graph:
            graph[airport].sort(reverse=True)

        result = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            result.append(airport)
            
        dfs('JFK')

        return result[::-1]