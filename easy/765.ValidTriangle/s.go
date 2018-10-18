/**
 * @param a: a integer represent the length of one edge
 * @param b: a integer represent the length of one edge
 * @param c: a integer represent the length of one edge
 * @return: whether three edges can form a triangle
 */
func isValidTriangle(a int, b int, c int) bool {
	// write your code here
	if (a+b > c) && (abs(a, b) < c) && (a+c > b) && (abs(a, c) < b) {
		return true
	}
	return false
}

func abs(a, b int) int {
	if a < b {
		return b - a
	}
	return a - b
}