package main

import "fmt"

func main() {
	A := &[]int{}
	fmt.Println(A)
	sortIntegers(A)

}

func sortIntegers(A *[]int) {
	// write your code here
	deA := *A
	if A == nil || len(deA) < 2 {
		return
	}
	//iterate over len of A
	for i := len(deA) - 1; i > 0; i-- {
		//iterate over elenements in a sub list
		for j := 0; j < i; j++ {
			//swap
			if deA[j] > deA[j+1] {
				deA[j], deA[j+1] = deA[j+1], deA[j]
			}
		}
	}
}
