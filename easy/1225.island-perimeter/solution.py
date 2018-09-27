class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                # if it is a piece of continent
                if grid[i][j] == 1:
                    # check which of the four edges are valid to
                    # increase the primeter by 1
                    
                    # conditions that left edge adds 1:
                    # left is boundry or it is water
                    if j==0 or grid[i][j-1] == 0:
                        perimeter+=1
                    # conditions that right edge adds 1:
                    # right is boundry or it is water
                    if j==cols-1 or grid[i][j+1] == 0:
                        perimeter+=1
                    # conditions that upper edge adds 1
                    # upper is boundry or it is water
                    if i==0 or grid[i-1][j] == 0:
                        perimeter+=1
                    # conditions that downside edge adds 1
                    # downside is boundry or it is water
                    if i==rows-1 or grid[i+1][j] == 0:
                        perimeter+=1                    
        return perimeter
    
