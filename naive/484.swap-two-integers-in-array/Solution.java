import java.util.Arrays;

public class Solution{
    public void swapIntegers(int[] A, int index1, int index2){
        if(index1 < 0 || index2 < 0 || index1 >= A.length|| index2 >= A.length){
            return;
        }
        int tmp = A[index1];        
        A[index1] = A[index2];
        A[index2] = tmp;
    }
    public static void main(String[] args){
        Solution mySolution = new Solution();
        int[] a = {1,5,60,2};
        mySolution.swapIntegers(a,1,30);
        System.out.println(Arrays.toString(a));
    }
}