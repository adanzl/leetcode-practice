"""
 * 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。
 * 不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。
 * 现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。
 * 假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。
 * 提示：
 * 1、1 <= n <= 5000
 * 2、rollMax.length == 6
 * 3、1 <= rollMax[i] <= 15
 * 链接：https://leetcode.cn/problems/dice-roll-simulation/
"""
from typing import List


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (i) for i in rollMax]  # end-len
        for i in range(6):
            dp[i][0] = 1
        for _ in range(n - 1):
            ndp = [[0] * (i) for i in rollMax]
            for e in range(6):  # end with e
                for pre in range(6):  # pre end
                    if e == pre:
                        for l in range(len(dp[e]) - 1):  # len
                            ndp[e][l + 1] += dp[e][l]
                            ndp[e][l + 1] %= MOD
                    else:
                        ndp[e][0] += sum(dp[pre])
                        ndp[e][0] %= MOD
            dp = ndp
        ans = 0
        for num in dp:
            ans += sum(num)
            ans %= MOD
        return ans


if __name__ == '__main__':
    # 1082
    print(Solution().dieSimulator(4, [2, 1, 1, 3, 3, 2]))
    # 34
    print(Solution().dieSimulator(2, [1, 1, 2, 2, 2, 3]))
    # 30
    print(Solution().dieSimulator(2, [1, 1, 1, 1, 1, 1]))
    # 181
    print(Solution().dieSimulator(3, [1, 1, 1, 2, 2, 3]))
