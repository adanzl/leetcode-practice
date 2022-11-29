"""
 * 给你一个 m x n 的二进制矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。
 * 提示：
 * 1、1 <= m, n <= 150
 * 2、mat[i][j] 仅包含 0 或 1
 * 链接：https://leetcode.cn/problems/count-submatrices-with-all-ones/
"""
from typing import List


class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        # 单调栈
        m, n = len(mat), len(mat[0])
        l = [[0] * n for _ in range(m)]  # 以mat[i][j] 为终点的连续1的长度
        ans = 0
        for j in range(n):
            s = []  # 递增栈 length-cnt
            total = 0
            for i in range(m):
                l[i][j] = 0 if mat[i][j] == 0 else (1 if j == 0 else l[i][j - 1] + 1)
                cnt = 1
                while s and s[-1][0] > l[i][j]:
                    sm, nn = s.pop()
                    total -= (sm - l[i][j]) * nn
                    cnt += nn
                s.append([l[i][j], cnt])
                total += l[i][j]
                ans += total
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
    # 24
    print(Solution().numSubmat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]))
