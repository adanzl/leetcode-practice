"""
 * 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
 * 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 k^n 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
 * 答案可能很大，你需要对 10^9 + 7 取模 。
 * 提示：
 * 1、1 <= n, k <= 30
 * 2、1 <= target <= 1000
 * 链接：https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/
"""
from typing import *


class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = dict({0: 1})  # v-cnt
        for _ in range(n):  # n
            ndp = dict()
            for i in range(1, k + 1):  # score
                for key, val in dp.items():
                    ndp[key + i] = (ndp.get(key + i, 0) + val) % MOD
            dp = ndp
        return dp.get(target, 0)


if __name__ == '__main__':
    # 0
    print(Solution().numRollsToTarget(1, 2, 3))
    # 6
    print(Solution().numRollsToTarget(2, 6, 7))
    # 1
    print(Solution().numRollsToTarget(1, 6, 3))
    # 222616187
    print(Solution().numRollsToTarget(30, 30, 500))
