package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	fmt.Println(reverseStr(110))

}

func reverse(number int) int {
	n := abs(number)
	result := 0
	for n > 0 {
		result *= 10
		result += n % 10
		n = int(math.Floor(float64(n) / float64(10)))
	}
	if number >= 0 {
		return result
	}
	return -result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func reverseStr(number int) int {
	n := abs(number)
	nStr := strconv.Itoa(n)
	runes := []rune(nStr)
	for i, j := 0, len(nStr)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	n, err := strconv.Atoi(string(runes))
	if err != nil {
		return 0
	}
	if number >= 0 {
		return n
	}
	return -n
}
