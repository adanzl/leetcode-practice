"""
* 给你一个下标从 0 开始的整数数组 players ，其中 players[i] 表示第 i 名运动员的 能力 值，同时给你一个下标从 0 开始的整数数组 trainers ，
* 其中 trainers[j] 表示第 j 名训练师的 训练能力值 。
* 如果第 i 名运动员的能力值 小于等于 第 j 名训练师的能力值，那么第 i 名运动员可以 匹配 第 j 名训练师。除此以外，每名运动员至多可以匹配一位训练师，每位训练师最多可以匹配一位运动员。
* 请你返回满足上述要求 players 和 trainers 的 最大 匹配数。
* 提示：
* 1、1 <= players.length, trainers.length <= 10^5
* 2、1 <= players[i], trainers[j] <= 10^9
* 链接：https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/
"""

from typing import *


class Solution:

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        idx1, idx2 = 0, 0
        while idx2 < len(trainers):
            if idx1 < len(players) and trainers[idx2] >= players[idx1]:
                idx1 += 1
            idx2 += 1
        return idx1


if __name__ == '__main__':
    # 2
    print(Solution().matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
    # 1
    print(Solution().matchPlayersAndTrainers([1, 1, 1], [10]))
