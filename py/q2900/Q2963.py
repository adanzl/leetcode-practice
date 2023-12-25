"""
 * 给你一个下标从 0 开始、由 正整数 组成的数组 nums。
 * 将数组分割成一个或多个 连续 子数组，如果不存在包含了相同数字的两个子数组，则认为是一种 好分割方案 。
 * 返回 nums 的 好分割方案 的 数目。
 * 由于答案可能很大，请返回答案对 10^9 + 7 取余 的结果。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/count-the-number-of-good-partitions/
"""
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

comb = lambda n, k: fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD


class Solution:

    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        nn = {}
        for i, num in enumerate(nums):
            if num in nn:
                nn[num][1] = i
            else:
                nn[num] = [i, i]
        st = sorted([[l, r, k] for k, (l, r) in nn.items()])
        arr = [st[0][:2]]
        for i in range(1, len(st)):
            if st[i][0] <= arr[-1][1]:
                arr[-1][1] = max(arr[-1][1], st[i][1])
            else:
                arr.append(st[i][:2])
        ans = 0
        nn = len(arr)
        for ii in range(nn):
            ans = (ans + comb(nn - 1, ii)) % MOD
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().numberOfGoodPartitions([1, 2, 3, 4]))
    # 1
    print(Solution().numberOfGoodPartitions([1, 1, 1, 1]))
    # 2
    print(Solution().numberOfGoodPartitions([1, 2, 1, 3]))
