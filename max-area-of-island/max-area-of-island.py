class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find_max_area(grid, i, j):
            size_ = 0
            if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[0])):
                return size_
​
            if grid[i][j] == 0:
                return size_
​
            grid[i][j] = 0
            size_ += find_max_area(grid, i+1, j)
            size_ += find_max_area(grid, i-1, j)
            size_ += find_max_area(grid, i, j+1)
            size_ += find_max_area(grid, i, j-1)
​
            return 1+size_
        
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_size = max(max_size, find_max_area(grid, i, j))
        return max_size
