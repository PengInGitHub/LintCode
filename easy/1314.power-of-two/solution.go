/**
 * @param n: an integer
 * @return: if n is a power of two
 */
func isPowerOfTwo(n int) bool {
	// Write your code here
	if n == 0 {
		return false
	}
	for n != 1 {
		if n%2 != 0 {
			return false
		}
		n = n / 2
	}
	return true
}
