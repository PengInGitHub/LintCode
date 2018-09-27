class Solution:
    """
    @param num: an integer
    @return: the complement number
    """
    def findComplement1(self, num):
        # Write your code here
        bin = "{0:b}".format(num)
        res = bin.replace('0', 'tmp').replace('1', '0').replace('tmp', '1')
        return int(res,2)

    def findComplement2(self, num):
        # double asterisk (**) is defined as exponentiation operator
        return num ^ 2 ** (len(bin(num))-2) - 1

    def findComplement(self, num):
        a = ''.join(str(1-int(i)) for i in bin(num)[2:])
        return int(a,2)
