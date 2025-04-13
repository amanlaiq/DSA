class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if ( r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1):
                        continue
                    
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
