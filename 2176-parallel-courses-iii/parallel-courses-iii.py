class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)
        
        memo = [-1] * n

        def cal(course):
            if memo[course] != -1:
                return memo[course]
            
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]
            max_prereq_time = 0
            for prereq in graph[course]:
                max_prereq_time = max(max_prereq_time, cal(prereq))

            memo[course] = time[course] + max_prereq_time
            return memo[course]
        
        overall_time = 0
        for course in range(n):
            overall_time = max(overall_time, cal(course))
        
        return overall_time