/**
 * @param J: the types of stones that are jewels
 * @param S: representing the stones you have
 * @return: how many of the stones you have are also jewels
 */
func numJewelsInStones(J string, S string) int {
	// Write your code here
	count := 0
	for j := 0; j < len(J); j++ {
		for s := 0; s < len(S); s++ {
			if J[j] == S[s] {
				count++
			}
		}
	}
	return count
}
