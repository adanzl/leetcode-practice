"""
 * 给你一个整数数组 colors ，它表示一个由红色和蓝色瓷砖组成的环，第 i 块瓷砖的颜色为 colors[i] ：
 * 1、colors[i] == 0 表示第 i 块瓷砖的颜色是 红色 。
 * 2、colors[i] == 1 表示第 i 块瓷砖的颜色是 蓝色 。
 * 环中连续 3 块瓷砖的颜色如果是 交替 颜色（也就是说中间瓷砖的颜色与它 左边 和 右边 的颜色都不同），那么它被称为一个 交替 组。
 * 请你返回 交替 组的数目。
 * 注意 ，由于 colors 表示一个 环 ，第一块 瓷砖和 最后一块 瓷砖是相邻的。
 * 提示：
 * 1、3 <= colors.length <= 100
 * 2、0 <= colors[i] <= 1
 * 链接：https://leetcode.cn/problems/alternating-groups-i/
"""
from typing import List


class Solution:

    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans, n = 0, len(colors)
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[i] != colors[(i - 1 + n) % n]:
                ans += 1
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().numberOfAlternatingGroups([1, 1, 1]))
    # 3
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1]))
