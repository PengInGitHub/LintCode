/**
 * @param num: an integer
 * @return: whether the integer is a power of 4
 */
func isPowerOfFour(num int) bool {
	// Write your code here
	if num == 0 {
		return false
	}
	for num != 1 {
		if num%4 != 0 {
			return false
		}
		num = num / 4
	}
	return true
}
