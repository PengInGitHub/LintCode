public class Solution {
    /**
     * @param n: a decimal number
     * @param k: a Integer represent base-k
     * @return: a base-k number
     */
    public String hexConversion(int n, int k) {
        // write your code here
        if(n==0)    return"0";
        StringBuffer sb=new StringBuffer();
        while(n!=0){
            char s;
            int temp=n%k;
            System.out.println("n:"+n+"k:"+k + "temp:"+temp);
            if(temp>=10){
                s=(char)(55+temp);
            }else{
                s=(char)(48+temp);
            }
            System.out.println("s:"+s);
            sb.append(s);
            System.out.println("sb:"+sb);
            n=n/k;
        }
        return sb.reverse().toString();
    }
    public static void main(String[] args){
        Solution s = new Solution();
        String str = s.hexConversion(135, 2);
        System.out.print(str);
    }
}
