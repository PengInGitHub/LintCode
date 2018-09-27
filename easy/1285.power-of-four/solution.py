class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        if num == 0:
            return False
        while num != 1:
            if num%4 != 0:
                return False
            num = num/4
        return True
        

        
