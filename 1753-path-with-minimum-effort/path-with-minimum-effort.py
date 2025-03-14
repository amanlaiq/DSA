class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visit = set()

        minheap = [[0,0,0]]
        directions =[[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minheap:
            diff, r, c = heapq.heappop(minheap)

            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            for dr,dc in directions:
                row, col = dr + r, dc + c
                if( row < 0 or col < 0 or row == rows or cols == col or (row, col) in visit):
                    continue
                newdiff = max(diff, abs(heights[r][c] - heights[row][col]))
                heapq.heappush(minheap, [newdiff, row, col])