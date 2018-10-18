/**
 * @param words: the given list of words
 * @return: the number of different transformations among all words we have
 
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
 */
 
 import(
    "fmt"
    ) 
func uniqueMorseRepresentations (words []string) int {
    // Write your code here
    var morse []string
    for _, word := range words{
        morse = append(morse, getMorse(word))
    }
    for _, v := range morse{
        fmt.Println(v)    
    }
    
    return countUnique(morse)
}

func getMorse(word string) string{
    morse := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    
    res := ""
    for _, char := range word{
        res += morse[indexOf(string(char))]
    }
    return res
}

func indexOf(char string) int{
    alpha := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"} 
    for p, v := range alpha{
        if char == v{
            return p
        }
        if char == "{
            continue
        }
    }
    fmt.Println("why here? ", char) 
    return 0
}

func countUnique(str []string) int{
    counter := make(map[string]int)
    for _, s := range str{
        counter[s] ++
    }
    return len(counter)
}