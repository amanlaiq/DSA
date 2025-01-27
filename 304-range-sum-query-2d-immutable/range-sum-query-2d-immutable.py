class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            return

        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build the prefix sum matrix
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                self.prefix_sum[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.prefix_sum[r - 1][c]    # Sum from the top
                    + self.prefix_sum[r][c - 1]    # Sum from the left
                    - self.prefix_sum[r - 1][c - 1]  # Remove double-counted area
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Adjust the indices because prefix_sum is 1-indexed
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Compute the region sum using the prefix sum matrix
        return (
            self.prefix_sum[row2][col2]
            - self.prefix_sum[row1 - 1][col2]
            - self.prefix_sum[row2][col1 - 1]
            + self.prefix_sum[row1 - 1][col1 - 1]
        )
