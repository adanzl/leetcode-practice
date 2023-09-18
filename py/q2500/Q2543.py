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
        # 从终点倒着走，那么 (x,y) 可以移动到 (x,x+y)、(x+y,y)、(x/2,y)、(x,y/2) 这些位置，后两个移动只有偶数才能除以 2。
        # 不断循环直到 x=y 且均为奇数（此时无法移动）：
        # 只要有偶数就除以 2。
        # 如果都为奇数，比如 x<y，那么走两步可以得到 (x,(x+y)/2)，这里修改 y 是因为 x < (x+y)/2 < y。
        # 那么总是可以让 x 和 y 不断变小。循环结束时如果 x=y=1，则说明可以做到。
        g = gcd(targetX, targetY)
        return g & (g - 1) == 0


# @lc code=end

if __name__ == '__main__':
    # False
    print(Solution().isReachable(6, 9))
    # True
    print(Solution().isReachable(4, 7))
