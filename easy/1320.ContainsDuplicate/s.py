class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        return len(set(nums)) != len(nums)
       
    def containsDuplicate2(self, nums):
        # Write your code here
        # use set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False