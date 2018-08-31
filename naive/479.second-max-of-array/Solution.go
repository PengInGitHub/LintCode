package main

func main() {

}

/**
 * @param nums: An integer array
 * @return: The second max number in the array.
 */
func secondMax(nums []int) int {
	// write your code here
	max, secMax := nums[0], nums[1]
	if max < secMax {
		max, secMax = secMax, max
	}
	for i, value := range nums {
		if i > 1 {
			if max < value {
				secMax = max
				max = value
			} else if secMax < value {
				secMax = value
			}
		}
	}
	return secMax
}
