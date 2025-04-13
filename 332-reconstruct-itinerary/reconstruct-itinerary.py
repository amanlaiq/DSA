class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)

        stack = ['JFK']
        res = []

        while stack:
            curr_element = stack[-1]
            if graph[curr_element]:
                stack.append(graph[curr_element].pop())
            else:
                res.append(stack.pop())

        return res[::-1]