class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits1(self, n):
        # Write your code here
        b = bin(n)
        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                return False
        return True
    def hasAlternatingBits(self, n):
        # Write your code here
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in xrange(len(bits)-1))