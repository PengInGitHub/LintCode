public class Solution {
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */

    // stirng version 
    public int reverseInteger(int number) {
        int tmp = Math.abs(number);
        String tmp_str = String.valueOf(tmp);
        StringBuffer sb = new StringBuffer(tmp_str);
        String sb_str = sb.reverse().toString();
        int tmp_int = Integer.parseInt(sb_str);
        if(tmp_int/number>=0){
            return tmp_int;
        }
        return -tmp_int;
    }

    //calculate residual 
    public int reverseIntegerRes(int number){
        int res = 0;
        int n = Math.abs(number);
        while (n>0){
            res *= 10;
            res += n%10;
            n /= 10;
        }
        return (int)x>=0? res:-res;
    }
}