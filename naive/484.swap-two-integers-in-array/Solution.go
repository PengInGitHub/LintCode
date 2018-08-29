package main

import (
	"fmt"
)

func main() {
	a := []int{1, 3, 5, 2}
	swapIntegers(&a, 1, -1)
	fmt.Println(a)
}

func swapIntegers(A *[]int, index1, index2 int) {
	p := *A
	if index1 >= len(p) || index2 >= len(p) || index1 < 0 || index2 < 0 {
		return
	}
	p[index1], p[index2] = p[index2], p[index1]
	A = &p
}
