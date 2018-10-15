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
    
    def reverseIntStr2(self, number):
        n_str = str(abs(number))
        if number < 0:
            return -int(n_str[::-1])
        else:
            return int(n_str[::-1])
        
    def reverseIntStr3(self, num):
        if num > 0:
            return int("".join(reversed(str(num))))
        else:
            return -int("".join(reversed(str(abs(num)))))
    
    
sol = Solution()
print sol.reverseIntStr3(-203)