/**
 * @param nums: the given array
 * @return: if any value appears at least twice in the array
 */
func containsDuplicate(nums []int) bool {
	// Write your code here
	seen := make(map[int]bool)
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		} else {
			seen[num] = true
		}
	}
	return false
}
