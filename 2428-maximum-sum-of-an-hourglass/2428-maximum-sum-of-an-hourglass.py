class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_sum = 0

        for i in range(0, row-2):
            for j in range(0, col-2):
                cs = 0
                cs += grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

                max_sum = max(max_sum, cs)
        return max_sum