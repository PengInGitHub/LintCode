#reference
#https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/191._number_of_1_bits.md
#https://www.jianshu.com/p/a60fa4243300
class Solution:
    """
    @param n: an unsigned integer
    @return: the number of â1' bits
    """
    def hammingWeight1(self, n):
        # write your code here
        #make use the law of decimal system (10-based) to binary system (2-based)
        #if n%2 has residual of 1, then it has 1
        counter = 0
        while(n != 0):
            if(n % 2 == 1):
                counter += 1
            n = n//2

        return counter

    def hammingWeight(self, n):
        return bin(n).count('1')
    
        def hammingWeight1(self, n):
        # write your code here
        counter = 0
        while n > 0:
            if n%2 == 1:
                counter += 1
            n /= 2
        return counter
    