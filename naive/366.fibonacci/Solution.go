package Solution

func fibonacci(n int) int {
	// write your code here
	if n == 1 || n == 2 {
		return n - 1
	}
	//min(n) = 3
	first, second, counter := 0, 1, 3
	next := first + second
	for counter < n {
		first, second = second, next
		next = first + second
		counter++
	}
	return next
}
