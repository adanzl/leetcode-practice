"""
 * Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。
 * Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。比赛一直持续到所有石头都被拿走。
 * 每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。
 * 假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回 "Tie" 。
 * 提示：
 * 1、1 <= values.length <= 50000
 * 2、-1000 <= values[i] <= 1000
 * 链接：https://leetcode.cn/problems/stone-game-iii/
"""
from typing import List


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # 递推
        inf = 0x3c3c3c3c
        n, total = len(stoneValue), sum(stoneValue)
        suffix_sum = [0] * (n + 1)
        dp = [-inf] * n + [0]
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]
            sm = 0
            for j in range(min(3, n - i)):  # 扩展个数
                sm += stoneValue[i + j]
                dp[i] = max(dp[i], sm + suffix_sum[i + j + 1] - dp[i + j + 1])
        v = dp[0]
        return 'Tie' if v == total / 2 else ('Alice' if v > total / 2 else 'Bob')

    def stoneGameIII1(self, stoneValue: List[int]) -> str:
        # 记忆
        n, total = len(stoneValue), sum(stoneValue)
        inf = 0x3c3c3c3c
        mem = {}

        def dfs(idx: int, total) -> int:
            if idx in mem: return mem[idx]
            if n <= idx: return 0
            ret, sm = -inf, 0
            for i in range(min(3, n - idx)):
                sm += stoneValue[idx + i]
                ret = max(ret, sm + total - dfs(idx + i + 1, total - sm))
            mem[idx] = ret
            return ret

        v = dfs(0, total)
        return 'Tie' if v == total / 2 else ('Alice' if v > total / 2 else 'Bob')


if __name__ == '__main__':
    # Bob
    print(Solution().stoneGameIII([1, 2, 3, 7]))
    # Tie
    print(Solution().stoneGameIII([-1, -2, -3]))
    # Alice
    print(Solution().stoneGameIII([1, 2, 3, -9]))
    # Tie
    print(Solution().stoneGameIII([1, 2, 3, 6]))
    # Alice
    print(Solution().stoneGameIII([1, 2, 3, -1, -2, -3, 7]))
