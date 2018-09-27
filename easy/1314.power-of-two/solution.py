class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if n == 0:
            return False
        while n!=1:
            if n%2 != 0:
                return False
            n = n/2
        return True
