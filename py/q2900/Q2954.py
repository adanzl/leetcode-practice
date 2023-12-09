"""
 * 给你一个整数 n 和一个下标从 0 开始的整数数组 sick ，数组按 升序 排序。
 * 有 n 位小朋友站成一排，按顺序编号为 0 到 n - 1 。数组 sick 包含一开始得了感冒的小朋友的位置。
 * 如果位置为 i 的小朋友得了感冒，他会传染给下标为 i - 1 或者 i + 1 的小朋友，前提 是被传染的小朋友存在且还没有得感冒。
 * 每一秒中， 至多一位 还没感冒的小朋友会被传染。
 * 经过有限的秒数后，队列中所有小朋友都会感冒。感冒序列 指的是 所有 一开始没有感冒的小朋友最后得感冒的顺序序列。
 * 请你返回所有感冒序列的数目。
 * 由于答案可能很大，请你将答案对 10^9 + 7 取余后返回。
 * 注意，感冒序列 不 包含一开始就得了感冒的小朋友的下标。
 * 提示：
 * 1、2 <= n <= 10^5
 * 2、1 <= sick.length <= n - 1
 * 3、0 <= sick[i] <= n - 1
 * 4、sick 按升序排列。
 * 链接：https://leetcode.cn/problems/count-the-number-of-infection-sequences/
"""
from itertools import pairwise
from typing import List

MOD = 1_000_000_007
MX = 100_000
# 组合数模板
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_fac = [0] * MX
inv_fac[MX - 1] = pow(fac[MX - 1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD


def comb(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


class Solution:

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        m = len(sick)
        total = n - m
        # 假设有三个感冒序列，长度分别为 k1,k2,k3，长度之和为 s。先从 s 个位置中选 k1 个位置放第一个感冒序列，这有 C(s, k1) 种放法。
        # 然后从 s−k1 个位置中选 k2 个位置放第二个感冒序列，这有 C(s−k1, k2) 种放法。
        # 然后从 s−k1−k2 个位置中选 k3 个位置放第三个感冒序列，这有 C(s−k1−k2, k3) 种放法。
        # 根据乘法原理，把所有放法相乘，再乘上每种感冒序列的方案，即为答案。
        ans = comb(total, sick[0]) * comb(total - sick[0], n - sick[-1] - 1) % MOD
        total -= sick[0] + n - sick[-1] - 1
        e = 0
        for p, q in pairwise(sick):
            k = q - p - 1
            if k:
                e += k - 1
                ans = ans * comb(total, k) % MOD
                total -= k
        return ans * pow(2, e, MOD) % MOD


if __name__ == '__main__':
    # 4
    print(Solution().numberOfSequence(5, sick=[0, 4]))
    # 3
    print(Solution().numberOfSequence(4, sick=[1]))
