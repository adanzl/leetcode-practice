"""
 * 给你一个大小为 m x n 的二进制矩阵 mat ，请你找出包含最多 1 的行的下标（从 0 开始）以及这一行中 1 的数目。
 * 如果有多行包含最多的 1 ，只需要选择 行下标最小 的那一行。
 * 返回一个由行下标和该行中 1 的数量组成的数组。
 * 提示：
 * 1、m == mat.length 
 * 2、n == mat[i].length 
 * 3、1 <= m, n <= 100 
 * 4、mat[i][j] 为 0 或 1
 * 链接：https://leetcode.cn/problems/row-with-maximum-ones/
"""
from collections import Counter
from typing import List


class Solution:

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        ri, rc = 0, 0
        for i in range(m):
            c = Counter(mat[i])
            if c[1] > rc:
                ri, rc = i, c[1]
        return [ri, rc]


if __name__ == '__main__':
    # [0,1]
    print(Solution().rowAndMaximumOnes([[0, 1], [1, 0]]))
    # [1,2]
    print(Solution().rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
    # [1,2]
    print(Solution().rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))
