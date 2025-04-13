class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visit = set((0,0))
        N = len(grid)
        minH = [[grid[0][0], 0, 0]]

        # visit.add((0,0))
        while minH:
            t, row, col = heapq.heappop(minH)

            if row == N - 1 and col == N - 1:
                return t

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if ( r < 0 or
                     c < 0 or 
                     r == N or
                     c == N or 
                     (r, c) in visit
                     ):
                     continue
                visit.add((r, c))
                heapq.heappush(minH, (max(t, grid[r][c]), r, c))
        
