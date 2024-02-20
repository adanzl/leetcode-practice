"""
 * 给你一个下标从 0 开始、大小为 m x n 的整数矩阵 matrix ，新建一个下标从 0 开始、名为 answer 的矩阵。
 * 使 answer 与 matrix 相等，接着将其中每个值为 -1 的元素替换为所在列的 最大 元素。
 * 返回矩阵 answer 。
 * 提示：
 * 1、m == matrix.length
 * 2、n == matrix[i].length
 * 3、2 <= m, n <= 50
 * 4、-1 <= matrix[i][j] <= 100
 * 5、测试用例中生成的输入满足每列至少包含一个非负整数。
 * 链接：https://leetcode.cn/problems/modify-the-matrix/
"""
from typing import List


class Solution:

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[0] * n for _ in range(m)]
        mx_col = [0] * n
        for i in range(m):
            for j in range(n):
                mx_col[j] = max(mx_col[j], matrix[i][j])
        for i in range(m):
            for j in range(n):
                ans[i][j] = matrix[i][j] if matrix[i][j] != -1 else mx_col[j]
        return ans


if __name__ == '__main__':
    # [[1,2,9],[4,8,6],[7,8,9]]
    print(Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]))
    # [[3,2],[5,2]]
    print(Solution().modifiedMatrix([[3, -1], [5, 2]]))
