"""
 * 你正在玩一个单人游戏，面前放置着大小分别为 a、b 和 c 的 三堆 石子。
 * 每回合你都要从两个 不同的非空堆 中取出一颗石子，并在得分上加 1 分。当存在 两个或更多 的空堆时，游戏停止。
 * 给你三个整数 a 、b 和 c ，返回可以得到的 最大分数 。
 * 提示：1 <= a, b, c <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-score-from-removing-stones/
"""
from typing import List


class Solution:

    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a <= c - b: return a + b
        return c + (a - c + b) // 2


if __name__ == '__main__':
    # 6
    print(Solution().maximumScore(2, 4, 6))
    # 7
    print(Solution().maximumScore(4, 4, 6))
    # 8
    print(Solution().maximumScore(1, 8, 8))
