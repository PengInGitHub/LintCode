public class Solution {
    /**
     * @param J: the types of stones that are jewels
     * @param S: representing the stones you have
     * @return: how many of the stones you have are also jewels
     */
    public int numJewelsInStones(String J, String S) {
        // Write your code here
        int count = 0;
        for (int j=0;j<J.length();j++){
            for(int s=0;s<S.length();s++){
                if (J.charAt(j) == S.charAt(s)){
                    count++;
                }
            }
        }
        return count;
    }
}