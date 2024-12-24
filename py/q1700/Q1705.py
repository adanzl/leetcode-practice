"""
 * 有一棵特殊的苹果树，一连 n 天，每天都可以长出若干个苹果。
 * 在第 i 天，树上会长出 apples[i] 个苹果，这些苹果将会在 days[i] 天后（也就是说，第 i + days[i] 天时）腐烂，
 * 变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 apples[i] == 0 且 days[i] == 0 表示。
 * 你打算每天 最多 吃一个苹果来保证营养均衡。注意，你可以在这 n 天之后继续吃苹果。
 * 给你两个长度为 n 的整数数组 days 和 apples ，返回你可以吃掉的苹果的最大数目。
 * 提示：
 * 1、apples.length == n
 * 2、days.length == n
 * 3、1 <= n <= 2 * 10^4
 * 4、0 <= apples[i], days[i] <= 2 * 10^4
 * 5、只有在 apples[i] = 0 时，days[i] = 0 才成立
 * 链接：https://leetcode.cn/problems/maximum-number-of-eaten-apples/
"""

from heapq import heappop, heappush
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1705 lang=python3
# @lcpr version=20004
#
# [1705] 吃苹果的最大数目
#


# @lc code=start
class Solution:

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        h = []
        for i, (a, d) in enumerate(zip(apples, days)):
            if a :
                heappush(h, [i + d, a])
            while h and (h[0][0] <= i or h[0][1] == 0):
                heappop(h)
            if h:
                ans += 1
                h[0][1] -= 1
        ts = len(apples)
        while h:
            a, d = heappop(h)
            v = max(0, min(a - ts, d))
            ans += v
            ts += v
        return ans


# @lc code=end

if __name__ == '__main__':
    # 5
    print(Solution().eatenApples([3, 0, 0, 0, 0, 2], days=[3, 0, 0, 0, 0, 2]))
    # 7
    print(Solution().eatenApples([1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
    #
    # print(Solution().eatenApples())
