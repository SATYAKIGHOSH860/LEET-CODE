class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(len(mat)):
            total += mat[i][i]

            if i != n - 1 - i:
                total+=mat[i][n-1-i]


        return total
