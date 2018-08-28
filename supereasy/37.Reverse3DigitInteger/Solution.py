class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        n = abs(number)
        result = 0
        while n>0:
            result *= 10
            result += n%10
            n = n//10
        if number>=0:
            return result
        return -result

    def reverseIntStr(self, number):
        n = abs(number)
        num_str = str(n)
        res = int(num_str[::-1])
        if number>=0:
            return res
        return -res

sol = Solution()
print sol.reverseIntStr(20)