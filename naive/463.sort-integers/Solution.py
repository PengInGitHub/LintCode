class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    #bubble sort
    def sortIntegers(self, A):
        # write your code here
        if A==None or len(A)<2:
            return
        for i in range(len(A)-1,0,-1):
            #mistake made here
            #for i in range(len(A)-1,0):
            #forgot range(len(A)-a,0)
            for j in range(i):
                if A[j]>A[j+1]:
                    #swap
                    tmp=A[j]
                    A[j]=A[j+1]
                    A[j+1]=tmp

solution = Solution()
A = [3,5,2,4,1]
solution.sortIntegers(A)
print(A)