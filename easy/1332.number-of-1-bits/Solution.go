//ref
//https://stackoverflow.com/questions/13870845/converting-from-an-integer-to-its-binary-representation
//https://golang.org/pkg/strings/#Count

/**
 * @param n: an unsigned integer
 * @return: the number of â€™1' bits
 */
import (
	"strconv"
	"strings"
)

func hammingWeight1(n int)

func hammingWeight1(n int) int {
	// write your code here
	toBin := strconv.FormatInt(int64(n), 2)
	return strings.Count(toBin, "1")
}

func hammingWeight(n int) int{
	counter := 0
	for n > 0 {
		if n%2 == 1{
			counter++
		}
		n /= 2
	}
	return counter
}















func hammingWeight(n int) int {
	count := 0
	for n != 0 {
		if n%2 == 1 {
			count++
		}
		n = n / 2
	}
	return count
}
