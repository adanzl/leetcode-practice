"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums 和一个 正奇数 整数 k 。
 * x 个子数组的能量值定义为 
 * strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1 ，
 * 其中 sum[i] 是第 i 个子数组的和。更正式的，能量值是满足 1 <= i <= x 的所有 i 对应的 (-1)^(i+1) * sum[i] * (x - i + 1) 之和。
 * 你需要在 nums 中选择 k 个 不相交子数组 ，使得 能量值最大 。
 * 请你返回可以得到的 最大能量值 。
 * 注意，选出来的所有子数组 不 需要覆盖整个数组。
 * 提示：
 * 1、1 <= n <= 10^4
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、1 <= k <= n
 * 4、1 <= n * k <= 10^6
 * 5、k 是奇数。
 * 链接：https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays/
"""
from itertools import accumulate
from typing import List


class Solution:

    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MN = -10**20
        pre_sm = [0] + list(accumulate(nums))
        # 定义 f[i][j] 表示从 nums[0] 到 nums[j−1] 中选出 i 个不相交非空连续子数组的最大能量值。
        f = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(1, k + 1):
            f[i][i - 1] = mx = MN
            w = (k - i + 1) * (1 if i % 2 else -1)
            for j in range(i, n - k + i + 1):  # j 的上下界是因为其它子数组至少要选一个数
                mx = max(mx, f[i - 1][j - 1] - pre_sm[j - 1] * w)
                f[i][j] = max(f[i][j - 1], pre_sm[j] * w + mx)
        return f[k][n]


if __name__ == '__main__':
    # 22
    print(Solution().maximumStrength([1, 2, 3, -1, 2], k=3))
    # 64
    print(Solution().maximumStrength([12, -2, -2, -2, -2], k=5))
    # -1
    print(Solution().maximumStrength([-1, -2, -3], k=1))
