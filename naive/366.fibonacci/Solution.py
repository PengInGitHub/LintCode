class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n==1 or n==2:
            return n-1
        first, second, counter = 0, 1, 3
        next_val = first + second
        while counter<n:
            counter += 1
            first, second = second, next_val
            next_val = first + second
        return next_val
            
