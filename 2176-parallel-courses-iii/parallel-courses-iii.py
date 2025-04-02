class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)
        
        memo = [-1] * n

        def calculatetime(course):
            if memo[course] != -1:
                return memo[course]
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]
            
            max_prereq_time = 0
            for prereq in graph[course]:
                max_prereq_time = max(max_prereq_time, calculatetime(prereq))
            
            memo[course] = time[course] + max_prereq_time
            return memo[course]
        
        min_time = 0 
        for course in range(n):
            min_time = max(min_time, calculatetime(course))

        return min_time