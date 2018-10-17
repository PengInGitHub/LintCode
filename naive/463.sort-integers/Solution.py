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

    # bubble
    def bubble(self, A):
        if len(A) < 2:
            return A
        # two loops, outter loop trough len(A) reversely
        start, end, step = len(A)-1, 0, -1
        #outter loop
        for i in range(start, end, step):
            # inner loop compares and swap
            for j in range(i):
                #swap
                if A[j] > A[j+1]:
                   A[j], A[j+1] = A[j+1], A[j] 
        return A
    
    # merge sort
    # divide and conquer
    # cut into pieces then merge
    def merge(self, left, right):
        print 'left:', left
        print 'right:', right
        i, j = 0, 0
        # merge is not in place
        res = []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
            

    def mergeSort(self, seq):
        '''if len(A) < 2:
            return A
        mid = int(len(A)/2)
        left = self.mergeSort(A[:mid])
        right = self.mergeSort(A[mid:])
        return self.merge(left, right)'''

        if len(seq)<=1:
            return seq
        mid=int(len(seq)/2)
        left=self.mergeSort(seq[:mid])
        right=self.mergeSort(seq[mid:])
        return self.merge(left, right)
        

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

'''solution = Solution()
A = [21, -4, -1, -1, 0, 900, 25, 6, 21, 14]
print solution.mergeSort(A)'''


def mergeSortUpdate(aList):
    length = len(aList)
    if length<2:
        return aList
    mid = length/2
    left = mergeSortUpdate(aList[:mid])
    right = mergeSortUpdate(aList[mid:])

    return mergeUpdate(left, right)

def mergeUpdate(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

merged = mergeSortUpdate(A)
print(merged)  