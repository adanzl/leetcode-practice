"""
 * Alice 和 Bob 正在玩一个幻想战斗游戏，游戏共有 n 回合，每回合双方各自都会召唤一个魔法生物：火龙（F）、水蛇（W）或地精（E）。
 * 每回合中，双方 同时 召唤魔法生物，并根据以下规则得分：
 * 1、如果一方召唤火龙而另一方召唤地精，召唤 火龙 的玩家将获得一分。
 * 2、如果一方召唤水蛇而另一方召唤火龙，召唤 水蛇 的玩家将获得一分。
 * 3、如果一方召唤地精而另一方召唤水蛇，召唤 地精 的玩家将获得一分。
 * 如果双方召唤相同的生物，那么两个玩家都不会获得分数。
 * 给你一个字符串 s，包含 n 个字符 'F'、'W' 和 'E'，代表 Alice 每回合召唤的生物序列：
 * 1、如果 s[i] == 'F'，Alice 召唤火龙。
 * 2、如果 s[i] == 'W'，Alice 召唤水蛇。
 * 3、如果 s[i] == 'E'，Alice 召唤地精。
 * Bob 的出招序列未知，但保证 Bob 不会在连续两个回合中召唤相同的生物。
 * 如果在 n 轮后 Bob 获得的总分 严格大于 Alice 的总分，则 Bob 战胜 Alice。
 * 返回 Bob 可以用来战胜 Alice 的不同出招序列的数量。
 * 由于答案可能非常大，请返回答案对 10^9 + 7 取余 后的结果。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s[i] 是 'F'、'W' 或 'E' 中的一个。
 * 链接：https://leetcode.cn/problems/count-the-number-of-winning-sequences/
"""
from collections import defaultdict

INF = 0x3c3c3c3c3c3c3c3c3c

MOD = 10**9 + 7


class Solution:

    def countWinningSequences(self, s: str) -> int:
        # dp[i][j][k] 表示前 i 个回合，Bob 第 i 个回合出 k 的情况等下，Bob-Alice 获得的得分 j + n 的方案数
        # F:0,E:1,W:2,0>1>2>0
        score = {'F': 0, 'E': 1, 'W': 2}
        n = len(s)
        # dp = [[[0, 0, 0] for __ in range(n + n + 2)] for _ in range(n + 1)]
        dp = {0: {}, 1: {}, 2: {}, -1: {0: 1}}
        for i, c in enumerate(s):
            win_s, lose_s, duce_s = (score[c] - 1) % 3, (score[c] + 1) % 3, score[c]
            n_dp = {0: defaultdict(int), 1: defaultdict(int), 2: defaultdict(int), -1: defaultdict(int)}
            for k, v in dp[duce_s].items():
                n_dp[win_s][k + 1] += v
                n_dp[lose_s][k - 1] += v
            for k, v in dp[lose_s].items():
                n_dp[win_s][k + 1] += v
                n_dp[duce_s][k] += v
            for k, v in dp[win_s].items():
                n_dp[lose_s][k - 1] += v
                n_dp[duce_s][k] += v
            for k, v in dp[-1].items():
                n_dp[win_s][k + 1] += 1
                n_dp[lose_s][k - 1] += 1
                n_dp[duce_s][k] += 1
            dp = n_dp

        ans = 0
        for i in range(1, n + 1):
            ans += dp[0][i]
            ans += dp[1][i]
            ans += dp[2][i]
            ans %= MOD
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countWinningSequences("FFF"))
    # 18
    print(Solution().countWinningSequences("FWEFW"))
    #
    # print(Solution().countWinningSequences())
