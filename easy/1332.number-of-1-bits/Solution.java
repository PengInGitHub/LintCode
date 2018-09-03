//import org.apache.commons.lang3.StringUtils;

public class Solution {
    /**
     * @param n: an unsigned integer
     * @return: the number of â€™1' bits
    
    public int hammingWeight1(int n) {
        // write your code here
        String toBin = Integer.toBinaryString(n);
        return StringUtils.countMatches(toBin, "1");
    }
     */
    public int hammingWeight(int n) {
        // write your code here
        int count = 0;
        while (n != 0){
            if (n%2 == 1){
                count++;
            }
            n /= 2;
        }
        return count;
    }    
}