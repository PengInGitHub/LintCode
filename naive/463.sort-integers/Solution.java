public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers(int[] A) {
        // write your code here
        if(A==null || A.length<2){
            return;
        }
        for (int i=A.length-1;i>0;i--){
            for (int j=0; j<i; j++){
                if (A[j]>A[j+1]){
                    //swap
                    int tmp = A[j];
                    A[j]=A[j+1];
                    A[j+1] = tmp;
                }
            }
        }
    }
}