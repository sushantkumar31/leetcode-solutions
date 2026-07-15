class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0

        for i in range(n):
            sum += mat[i][i] + mat[i][n-1-i]

        if n%2 == 0:
            return sum
        return sum - mat[n//2][n//2]
        
        