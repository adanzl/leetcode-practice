"""
 * 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
 * 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
 * 1、覆盖所有 空 格子。
 * 2、不覆盖任何 被占据 的格子。
 * 3、我们可以放入任意数目的邮票。
 * 4、邮票可以相互有 重叠 部分。
 * 5、邮票不允许 旋转 。
 * 6、邮票必须完全在矩阵 内 。
 * 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[r].length
 * 3、1 <= m, n <= 10^5
 * 4、1 <= m * n <= 2 * 10^5
 * 5、grid[r][c] 要么是 0 ，要么是 1 。
 * 6、1 <= stampHeight, stampWidth <= 10^5
 * 链接：https://leetcode.com/problems/stamping-the-grid/
"""

from typing import List

#
# @lc app=leetcode.cn id=2132 lang=python3
#
# [2132] 用邮票贴满网格图
#


# @lc code=start
class Solution:

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]  # 二维前缀和
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + grid[i][j]
        ss = [[0] * (n + 1) for _ in range(m + 1)]  # 二维差分数组
        # b[i][j] = a[i][j] - a[i-1][j] - a[i][j-1] + a[i-1][j-1]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                s = pre_sum[i + stampHeight][j + stampWidth] - pre_sum[i + stampHeight][j] - pre_sum[i][j + stampWidth] + pre_sum[i][j]
                if s == 0:
                    ss[i + stampHeight][j + stampWidth] += 1
                    ss[i][j] += 1
                    ss[i][j + stampWidth] -= 1
                    ss[i + stampHeight][j] -= 1
        p_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                v = p_sum[i + 1][j] + p_sum[i][j + 1] - p_sum[i][j] + ss[i][j]
                p_sum[i + 1][j + 1] = v
                if v == 0 and grid[i][j] == 0:
                    return False
        return True


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().possibleToStamp([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], stampHeight=4, stampWidth=3))
    # False
    print(Solution().possibleToStamp([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], stampHeight=2, stampWidth=2))
