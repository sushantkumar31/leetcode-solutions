class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = []

        for i in range(col):
            l = []
            for j in range(row):
                l.append(matrix[j][i])
            ans.append(l)

        return ans