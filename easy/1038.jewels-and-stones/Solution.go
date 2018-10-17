/**
 * @param J: the types of stones that are jewels
 * @param S: representing the stones you have
 * @return: how many of the stones you have are also jewels
 */
func numJewelsInStones (J string, S string) int {
    // two loops, compare in inner loop
    counter := 0
    for _, j := range J{
        for _, s := range S{
            if j == s{
                counter ++
                }
            }
        }
    return counter
    }

