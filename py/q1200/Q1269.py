"""
 * 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。
 * 每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。
 * 给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。
 * 由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。
 * 提示：
 * 1、1 <= steps <= 500
 * 2、1 <= arrLen <= 10^6
 * 链接：https://leetcode.cn/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
"""


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * steps
        dp[0] = 1
        for _ in range(steps):
            ndp = [0] * steps
            for j in range(min(arrLen, steps)):
                if j > 0: ndp[j] += dp[j - 1]
                if j < steps - 1: ndp[j] += dp[j + 1]
                ndp[j] += dp[j]
            dp = ndp
        return dp[0] % MOD


if __name__ == '__main__':
    # 4
    print(Solution().numWays(3, 2))
    # 2
    print(Solution().numWays(2, 4))
    # 8
    print(Solution().numWays(4, 2))
