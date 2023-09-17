"""
 * 给你一个无穷大的网格图。一开始你在 (1, 1) ，你需要通过有限步移动到达点 (targetX, targetY) 。
 * 每一步 ，你可以从点 (x, y) 移动到以下点之一：
 * 1、(x, y - x)
 * 2、(x - y, y)
 * 3、(2 * x, y)
 * 4、(x, 2 * y)
 * 给你两个整数 targetX 和 targetY ，分别表示你最后需要到达点的 X 和 Y 坐标。
 * 如果你可以从 (1, 1) 出发到达这个点，请你返回true ，否则返回 false 。
 * 提示：1 <= targetX, targetY <= 10^9
 * 链接：https://leetcode.cn/problems/check-if-point-is-reachable/
"""

from math import gcd

#
# @lc app=leetcode.cn id=2543 lang=python3
#
# [2543] 判断一个点是否可以到达
#


# @lc code=start
class Solution:

    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return g & (g - 1) == 0


# @lc code=end

if __name__ == '__main__':
    # False
    print(Solution().isReachable(6, 9))
    # True
    print(Solution().isReachable(4, 7))