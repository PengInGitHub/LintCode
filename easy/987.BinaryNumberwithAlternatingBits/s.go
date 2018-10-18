import (
	"strconv"
)

func hasAlternatingBits(n int) bool {
	// Write your code here
	bits := strconv.FormatInt(int64(n), 2)
	for i := 0; i < len(bits)-1; i++ {
		if bits[i] == bits[i+1] {
			return false
		}
	}
	return true
}