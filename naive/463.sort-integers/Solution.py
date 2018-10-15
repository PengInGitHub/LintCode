class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    # quick
    def sortIntegers1(self, A):
        if len(A) < 2:
            return A
        smaller, equal, larger = [], [], []
        pivot = A[0]
        
        for i in A:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                larger.append(i)
        
        return self.sortIntegers1(smaller) + equal + self.sortIntegers1(larger)


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
A = [21, -4, -1, -1, 0, 900, 25, 6, 21, 14]
print solution.sortIntegers1(A)
