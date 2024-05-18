"""
 * Alice 向一面非常大的墙上掷出 n 支飞镖。
 * 给你一个数组 darts ，其中 darts[i] = [x_i, y_i] 表示 Alice 掷出的第 i 支飞镖落在墙上的位置。
 * Bob 知道墙上所有 n 支飞镖的位置。他想要往墙上放置一个半径为 r 的圆形靶。
 * 使 Alice 掷出的飞镖尽可能多地落在靶上。
 * 给你整数 r ，请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。
 * 提示：
 * 1、1 <= darts.length <= 100
 * 2、darts[i].length == 2
 * 3、-10^4 <= x_i, y_i <= 10^4
 * 4、darts 中的元素互不相同
 * 5、1 <= r <= 5000
 * 链接：https://leetcode.cn/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/
"""

from typing import List

#
# @lc app=leetcode.cn id=1453 lang=python3
#
# [1453] 圆形靶内的最大飞镖数量
#


# @lc code=start
class Solution:

    def numPoints(self, darts: List[List[int]], r: int) -> int:
        ans = 1
        for i, p0 in enumerate(darts):
            for j in range(i + 1, len(darts)):
                p1 = darts[j]
                v = [p1[0] - p0[0], p1[1] - p0[1]]  # 方向向量
                d = (v[0]**2 + v[1]**2)**0.5  # 向量长度
                if d > 2 * r:
                    continue
                m = [(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2]  # 中点坐标
                v = [v[0] / d, v[1] / d]  # 单位向量
                dd = (r**2 - (d / 2)**2)**0.5  # 弓高
                d0, d1 = [v[1], -v[0]], [-v[1], -v[0]]  # 顺逆旋转
                c0, c1 = [m[0] + dd * d0[0], m[1] + dd * d0[1]], [m[0] + dd * d1[0], m[1] + dd * d1[1]]
                v0, v1 = 0, 0
                for p in darts:
                    if round((p[0] - c0[0])**2 + (p[1] - c0[1])**2) <= r**2:
                        v0 += 1
                    if round((p[0] - c1[0])**2 + (p[1] - c1[1])**2) <= r**2:
                        v1 += 1
                ans = max(ans, v0, v1)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().numPoints([[1, 2], [3, 5], [1, -1], [2, 3], [4, 1], [1, 3]], 2))
    # 4
    print(Solution().numPoints([[-2, 0], [2, 0], [0, 2], [0, -2]], r=2))
    # 5
    print(Solution().numPoints([[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5))
