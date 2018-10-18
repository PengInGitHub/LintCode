class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        # outter loop, iterate rows
        for row_idx in range(1, len(matrix)):
            # inner loop, iterate cols
            for col_idx in range(1, len(matrix[0])):
                if matrix[row_idx][col_idx] != matrix[row_idx-1][col_idx-1]:
                    return False
        return True
 
    def isToeplitzMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j not in groups:
                    groups[i-j] = matrix[i][j]
                elif groups[i-j] != matrix[i][j]:
                    return False
        return True    