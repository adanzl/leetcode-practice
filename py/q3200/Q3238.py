"""
 * 给你一个整数 n ，表示在一个游戏中的玩家数目。
 * 同时给你一个二维整数数组 pick ，其中 pick[i] = [xi, yi] 表示玩家 xi 获得了一个颜色为 yi 的球。
 * 1、如果玩家 i 获得的球中任何一种颜色球的数目 严格大于 i 个，那么我们说玩家 i 是胜利玩家。换句话说：
 * 2、如果玩家 0 获得了任何的球，那么玩家 0 是胜利玩家。
 * 3、如果玩家 1 获得了至少 2 个相同颜色的球，那么玩家 1 是胜利玩家。
 * 4、...
 * 5、如果玩家 i 获得了至少 i + 1 个相同颜色的球，那么玩家 i 是胜利玩家。
 * 请你返回游戏中 胜利玩家 的数目。
 * 注意，可能有多个玩家是胜利玩家。
 * 提示：
 * 1、2 <= n <= 10
 * 2、1 <= pick.length <= 100
 * 3、pick[i].length == 2
 * 4、0 <= xi <= n - 1 
 * 5、0 <= yi <= 10
 * 链接：https://leetcode.cn/problems/find-the-number-of-winning-players/
"""
from typing import Counter, List


class Solution:

    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = [Counter() for _ in range(n)]
        ans = 0
        for x, y in pick:
            cnt[x][y] += 1
        for i, c in enumerate(cnt):
            if c and c.most_common()[0][1] > i:
                ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().winningPlayerCount(4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]))
    # 0
    print(Solution().winningPlayerCount(5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]]))
    # 1
    print(Solution().winningPlayerCount(5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]]))
