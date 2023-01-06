"""
 * 给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。
 * 给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles[i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。
 * 比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。
 * 这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。
 * 比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
 * 这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。
 * 注意：点 0 处和点 n 处的任一跑道都不会有障碍。
 * 提示：
 * 1、obstacles.length == n + 1
 * 2、1 <= n <= 5 * 10^5
 * 3、0 <= obstacles[i] <= 3
 * 4、obstacles[0] == obstacles[n] == 0
 * 链接：https://leetcode.cn/problems/minimum-sideway-jumps/
"""
from typing import List


class Solution:

    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]
        inf = 0x3c3c3c3c
        for i in range(1, len(obstacles)):
            o = obstacles[i]
            ndp = [inf, inf, inf]
            if o != 1 and obstacles[i - 1] != 1:
                ndp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
            if o != 2 and obstacles[i - 1] != 2:
                ndp[1] = min(dp[1], dp[0] + 1, dp[2] + 1)
            if o != 3 and obstacles[i - 1] != 3:
                ndp[2] = min(dp[2], dp[0] + 1, dp[1] + 1)
            dp = ndp
        return min(dp)


if __name__ == '__main__':
    # 2
    print(Solution().minSideJumps([0, 1, 2, 3, 0]))
    # 0
    print(Solution().minSideJumps([0, 1, 1, 3, 3, 0]))
    # 2
    print(Solution().minSideJumps([0, 2, 1, 0, 3, 0]))
