class Solution(object):
    def countNegatives(self, grid):
        l = len(grid)
        count = 0
        for row in range(l):
            for item in grid[row]:
                if item < 0:
                    count += 1
        return count
            