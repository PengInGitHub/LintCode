public class Solution {
    /**
     * @param nums: An integer array
     * @return: The second max number in the array.
     */
    public int secondMax(int[] nums) {
        // write your code here
        int max = nums[0];
        int secondMax = nums[1];
        if (max < secondMax){
            int tmp = max;
            max = secondMax;
            secondMax = tmp;
        }
        for (int i=2;i<nums.length;i++){
            if (max<nums[i]){
                secondMax = max;
                max=nums[i];
            }else if(nums[i]>secondMax){
                secondMax = nums[i];
            }
        }
        return secondMax;
    }
}