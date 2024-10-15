"""
 * 给你一个整数数组 nums 和一个 正 整数 k 。
 * 定义长度为 2 * x 的序列 seq 的 值 为：
 * (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
 * 请你求出 nums 中所有长度为 2 * k 的 子序列 的 最大值 。
 * 提示：
 * 1、2 <= nums.length <= 400
 * 2、1 <= nums[i] < 2^7
 * 3、1 <= k <= nums.length / 2
 * 链接：https://leetcode.cn/problems/find-the-maximum-sequence-value-of-array/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # f[i][j][x] 表示前 i 个数，选 j 个，或值为 x 是否存在
        # f[i][j][x] = f[i-1][j-1]|nums[i-1] or f[i-i][j]
        f = [[[False] * (1 << 7) for _ in range(k + 1)] for __ in range(n + 1)]
        f1 = [[[False] * (1 << 7) for _ in range(k + 1)] for __ in range(n + 1)]

        for i in range(n):
            f[i][0][0] = True
            f1[i][0][0] = True
        for i in range(1, n + 1):  # 400 前 i 个
            for j in range(min(i, k), 0, -1):  # 400 取 j 个
                for num in range(1 << 7):  # 128
                    f[i][j][num] |= f[i - 1][j][num]
                    if f[i - 1][j - 1][num]:
                        f[i][j][num | nums[i - 1]] = True
                    f1[i][j][num] |= f1[i - 1][j][num]
                    if f1[i - 1][j - 1][num]:
                        f1[i][j][num | nums[n - i]] = True
        # split
        ans = 0
        for i in range(1, n):
            ia, ib = i, n - i
            for a in range(1, 1 << 7):
                if f[ia][k][a]:
                    for b in range(1, 1 << 7):
                        if f1[ib][k][b]:
                            ans = max(ans, a ^ b)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxValue([4, 2, 5, 6, 7], k=2))
    # 5
    print(Solution().maxValue([2, 6, 7], k=1))
    #
    # print(Solution().maxValue())
