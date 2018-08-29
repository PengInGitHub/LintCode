package main

/**
 * @param character: a character
 * @return: a character
 */
import (
	"fmt"
	"unicode"
)

func main() {
	fmt.Print(string(lowercaseToUppercase('a')))
}
func lowercaseToUppercase(character byte) byte {
	// write your code here
	return byte(unicode.ToUpper(rune(character)))
}
