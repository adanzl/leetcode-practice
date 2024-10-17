"""
 * 给你一个长度为 n 的二维整数数组 coordinates 和一个整数 k ，其中 0 <= k < n 。
 * coordinates[i] = [xi, yi] 表示二维平面里一个点 (xi, yi) 。
 * 如果一个点序列 (x1, y1), (x2, y2), (x3, y3), ..., (xm, ym) 满足以下条件，那么我们称它是一个长度为 m 的 上升序列 ：
 * 1、对于所有满足 1 <= i < m 的 i 都有 xi < xi + 1 且 yi < yi + 1 。
 * 2、对于所有 1 <= i <= m 的 i 对应的点 (xi, yi) 都在给定的坐标数组里。
 * 请你返回包含坐标 coordinates[k] 的 最长上升路径 的长度。
 * 提示：
 * 1、1 <= n == coordinates.length <= 10^5
 * 2、coordinates[i].length == 2
 * 3、0 <= coordinates[i][0], coordinates[i][1] <= 10^9
 * 4、coordinates 中的元素 互不相同 。
 * 5、0 <= k <= n - 1
 * 链接：https://leetcode.cn/problems/length-of-the-longest-increasing-path
"""

import bisect
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=3288 lang=python3
# @lcpr version=20001
#
# [3288] 最长上升路径的长度
#


# @lc code=start
class Solution:

    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        kx, ky = coordinates[k]
        # x 顺序，y 逆序，对于每个 x 只有最大的y生效，从而规避了x相同的情况
        coordinates.sort(key=lambda p: (p[0], -p[1]))

        g = []
        for x, y in coordinates:
            if x < kx and y < ky or x > kx and y > ky:
                j = bisect.bisect_left(g, y)
                if j < len(g):
                    g[j] = y
                else:
                    g.append(y)
        return len(g) + 1  # 算上 coordinates[k]


# @lc code=end

#

if __name__ == '__main__':
    # 3
    print(Solution().maxPathLength([[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]], k=1))
    # 2
    print(Solution().maxPathLength([[2, 1], [7, 0], [5, 6]], k=2))
    #
    # print(Solution().maxPathLength())
