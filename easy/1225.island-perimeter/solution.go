/**
 * @param grid: a 2D array
 * @return: the perimeter of the island
 */
func islandPerimeter(grid [][]int) int {
	// Write your code here
	perimeter := 0
	rows, cols := len(grid), len(grid[0])
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == 1 {
				if (i == 0) || (grid[i-1][j] == 0) {
					perimeter++
				}
				if i == rows-1 || grid[i+1][j] == 0 {
					perimeter++
				}
				if j == 0 || grid[i][j-1] == 0 {
					perimeter++
				}
				if j == cols-1 || grid[i][j+1] == 0 {
					perimeter++
				}
			}
		}
	}
	return perimeter
}
