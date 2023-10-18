"""
 * 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。
 * 子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。
 * 如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。
 * 提示：
 * 1、1 <= matrix.length <= 100
 * 2、1 <= matrix[0].length <= 100
 * 3、-1000 <= matrix[i] <= 1000
 * 4、-10^8 <= target <= 10^8
 * 链接：https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/
"""

from collections import Counter
from typing import List

#
# @lc app=leetcode.cn id=1074 lang=python3
#
# [1074] 元素和为目标值的子矩阵数量
#


# @lc code=start
class Solution:

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # 二维前缀和
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + matrix[i][j]

        # 结合一维前缀和
        for up in range(m):
            for down in range(up, m):
                cnt = Counter([0])
                sm = 0
                for right in range(n):
                    sm += pre_sum[down + 1][right + 1] + pre_sum[up][right] - pre_sum[up][right + 1] - pre_sum[down + 1][right]
                    ans += cnt[sm - target]
                    cnt[sm] += 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
    # 5
    print(Solution().numSubmatrixSumTarget([[1, -1], [-1, 1]], target=0))
    # 0
    print(Solution().numSubmatrixSumTarget([[904]], target=0))
