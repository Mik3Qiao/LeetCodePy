from typing import List


#
#
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         colFlag = [False] * len(matrix[0])
#         rowFlag = [False] * len(matrix)
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j] == 0:
#                     rowFlag[i] = True
#                     colFlag[j] = True
#
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if rowFlag[i] or colFlag[j]:
#                     matrix[i][j] = 0


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLength = len(matrix)
        colLength = len(matrix[0])

        result = []
        up = left = 0
        right = colLength - 1
        down = rowLength - 1
        while len(result) < rowLength * colLength:
            for col in range(left, right + 1):
                result.append(matrix[up][right])

            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            if up != down:
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            if left != right:
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
