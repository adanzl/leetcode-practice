"""
 * 给你一个整数数组 colors 和一个整数 k ，colors表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ：
 * 1、colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。
 * 2、colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。
 * 环中连续 k 块瓷砖的颜色如果是 交替 颜色（也就是说除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。
 * 请你返回 交替 组的数目。
 * 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。
 * 提示：
 * 1、3 <= colors.length <= 10^5
 * 2、0 <= colors[i] <= 1
 * 3、3 <= k <= colors.length
 * 链接：https://leetcode.cn/problems/alternating-groups-ii/
"""
from typing import List


class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans, n = 0, len(colors)
        v0, v1 = 0, 1
        ff = 0
        for i in range(k - 1):
            v0 = (v0 << 1) + (1 ^ (v0 & 1))
            v1 = (v1 << 1) + (1 ^ (v1 & 1))
        for i in range(k):
            ff = (ff << 1) + colors[i]

        for i in range(n):
            if ff == v0 or ff == v1:
                ans += 1
            ff = ((ff << 1) + colors[(i + k) % n]) & ((1 << k) - 1)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], k=3))
    # 2
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], k=6))
    # 0
    print(Solution().numberOfAlternatingGroups([1, 1, 0, 1], k=4))
