class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def find_jewels(J, S):
        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count += 1
        return count
  
    
    def numJewelsInStones(self, J, S):
        # Write your code here
        count = 0
        for c_j in J:
            for c_s in S:
                if c_s == c_j:
                    count += 1
        return count
