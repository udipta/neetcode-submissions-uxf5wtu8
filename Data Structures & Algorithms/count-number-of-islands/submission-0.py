class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # index out of bounds / water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return 0

            grid[i][j] = "0"
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
            return 1

        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += dfs(r, c)

        return count