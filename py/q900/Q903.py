"""
 * 给定一个长度为 n 的字符串 s ，其中 s[i] 是:
 * 1、“D” 意味着减少，或者
 * 2、“I” 意味着增加
 * 有效排列 是对有 n + 1 个在 [0, n]  范围内的整数的一个排列 perm ，使得对所有的 i：
 * 1、如果 s[i] == 'D'，那么 perm[i] > perm[i+1]，以及；
 * 2、如果 s[i] == 'I'，那么 perm[i] < perm[i+1]。
 * 返回 有效排列  perm的数量 。因为答案可能很大，所以请返回你的答案对 10^9 + 7 取余。
 * 提示:
 * 1、n == s.length
 * 2、1 <= n <= 200
 * 3、s[i] 不是 'I' 就是 'D'
 * 链接：https://leetcode.cn/problems/valid-permutations-for-di-sequence/
"""
from typing import *


class Solution:

    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]
        for i, c in enumerate(s, 1):
            ndp = [0] * (i + 1)
            if c == 'I':
                for num in range(i):
                    for j in range(num):
                        ndp[num] += dp[j]
                ndp[i] = sum(dp[:i]) % MOD
            else:
                for num in range(i):
                    for j in range(num, i):
                        ndp[num] += dp[j]
            dp = ndp
        return sum(dp) % MOD


if __name__ == '__main__':
    # 1
    print(Solution().numPermsDISequence("III"))
    # 5
    print(Solution().numPermsDISequence("DID"))