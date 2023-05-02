"""
 * 给你两个下标从 0 开始的整数数组 player1 和 player2 ，分别表示玩家 1 和玩家 2 击中的瓶数。
 * 保龄球比赛由 n 轮组成，每轮的瓶数恰好为 10 。
 * 假设玩家在第 i 轮中击中 xi 个瓶子。玩家第 i 轮的价值为：
 * 1、如果玩家在前两轮中击中了 10 个瓶子，则为 2xi 。
 * 2、否则，为 xi 。
 * 玩家的得分是其 n 轮价值的总和。
 * 返回
 * 1、如果玩家 1 的得分高于玩家 2 的得分，则为 1 ;
 * 2、如果玩家 2 的得分高于玩家 1 的得分，则为 2 ;
 * 3、如果平局，则为 0 。
 * 提示：
 * 1、n == player1.length == player2.length
 * 2、1 <= n <= 1000
 * 3、0 <= player1[i], player2[i] <= 10
 * 链接：https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/description/
"""
from typing import List


class Solution:

    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        def score(ss):
            ret = 0
            for i, s in enumerate(ss):
                if (i >= 1 and ss[i - 1] == 10) or (i >= 2 and ss[i - 2] == 10):
                    ret += s * 2
                else:
                    ret += s
            return ret

        s1, s2 = score(player1), score(player2)
        if s1 == s2: return 0
        return 1 if s1 > s2 else 2


if __name__ == '__main__':
    # 1
    print(Solution().isWinner([4, 10, 7, 9], player2=[6, 5, 2, 3]))
    # 2
    print(Solution().isWinner([3, 5, 7, 6], player2=[8, 10, 10, 2]))
    # 0
    print(Solution().isWinner([2, 3], player2=[4, 1]))
