"""
 * n 名运动员参与一场锦标赛，所有运动员站成一排，并根据 最开始的 站位从 1 到 n 编号
 * （运动员 1 是这一排中的第一个运动员，运动员 2 是第二个运动员，依此类推）。
 * 锦标赛由多个回合组成（从回合 1 开始）。
 * 每一回合中，这一排从前往后数的第 i 名运动员需要与从后往前数的第 i 名运动员比拼，获胜者将会进入下一回合。
 * 如果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。
 * 例如，当前回合中，运动员 1, 2, 4, 6, 7 站成一排
 * 1、运动员 1 需要和运动员 7 比拼
 * 2、运动员 2 需要和运动员 6 比拼
 * 3、运动员 4 轮空晋级下一回合
 * 每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。
 * 编号为 firstPlayer 和 secondPlayer 的运动员是本场锦标赛中的最佳运动员。
 * 在他们开始比拼之前，完全可以战胜任何其他运动员。
 * 而任意两个其他运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以 裁定 谁是这一回合的获胜者。
 * 给你三个整数 n、firstPlayer 和 secondPlayer 。
 * 返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的 最早 回合数和 最晚 回合数。
 * 提示：
 * 1、2 <= n <= 28
 * 2、1 <= firstPlayer < secondPlayer <= n
 * 链接：https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/
"""

from functools import cache
from typing import List

#
# @lc app=leetcode.cn id=1900 lang=python3
#
# [1900] 最佳运动员的比拼回合
#


# @lc code=start
class Solution:

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        @cache
        def dfs(n, f, s):
            if f + s == n + 1:
                return [1, 1]

            # F(n,f,s)=F(n,n+1-s,n+1-f)
            if f + s > n + 1:
                return dfs(n, n + 1 - s, n + 1 - f)

            earliest, latest = 0x3c3c3c3c3c3c, 0
            n_half = (n + 1) // 2

            if s <= n_half:
                # s 在左侧或者中间
                for i in range(f):
                    for j in range(s - f):
                        x, y = dfs(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                # s 在右侧
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dfs(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return [earliest + 1, latest + 1]

        return dfs(n, firstPlayer, secondPlayer)


# @lc code=end

if __name__ == '__main__':
    # [2,2]
    print(Solution().earliestAndLatest(4, 3, 4))
    # [2,2]
    print(Solution().earliestAndLatest(4, 1, 3))
    # [2,2]
    print(Solution().earliestAndLatest(3, 2, 3))
    # [3,4]
    print(Solution().earliestAndLatest(11, firstPlayer=2, secondPlayer=4))
    # [1,1]
    print(Solution().earliestAndLatest(5, firstPlayer=1, secondPlayer=5))
