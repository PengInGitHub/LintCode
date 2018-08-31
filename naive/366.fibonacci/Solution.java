public class Solution {
    /**
     * @param n: an integer
     * @return: an ineger f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        if(n==1 || n==2){
            return n-1;
        }
        int first = 0;
        int second = 1;
        int counter = 3;
        int next = first + second;
        while(counter<n){
            counter++;
            first = second;
            second = next;
            next = first + second;
        }
        return next;
    }
}