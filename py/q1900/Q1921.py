"""
 * 你正在玩一款电子游戏，在游戏中你需要保护城市免受怪物侵袭。
 * 给你一个 下标从 0 开始 且长度为 n 的整数数组 dist ，其中 dist[i] 是第 i 个怪物与城市的 初始距离（单位：米）。
 * 怪物以 恒定 的速度走向城市。给你一个长度为 n 的整数数组 speed 表示每个怪物的速度，其中 speed[i] 是第 i 个怪物的速度（单位：米/分）。
 * 怪物从 第 0 分钟 时开始移动。你有一把武器，并可以 选择 在每一分钟的开始时使用，包括第 0 分钟。
 * 但是你无法在一分钟的中间使用武器。这种武器威力惊人，一次可以消灭任一还活着的怪物。
 * 一旦任一怪物到达城市，你就输掉了这场游戏。如果某个怪物 恰 在某一分钟开始时到达城市，这会被视为 输掉 游戏，在你可以使用武器之前，游戏就会结束。
 * 返回在你输掉游戏前可以消灭的怪物的 最大 数量。如果你可以在所有怪物到达城市前将它们全部消灭，返回  n 。
 * 提示：
 * 1、n == dist.length == speed.length
 * 2、1 <= n <= 10^5
 * 3、1 <= dist[i], speed[i] <= 10^5
 * 链接：https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/
"""
from heapq import heapify, heappop
from typing import List


class Solution:

    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        h = [d / s for d, s in zip(dist, speed)]
        heapify(h)
        ans = 0
        while h:
            t = heappop(h)
            if t > ans:
                ans += 1
            else:
                break
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().eliminateMaximum([1, 3, 4], speed=[1, 1, 1]))
    # 1
    print(Solution().eliminateMaximum([1, 1, 2, 3], speed=[1, 1, 1, 1]))
    # 1
    print(Solution().eliminateMaximum([3, 2, 4], speed=[5, 3, 2]))
