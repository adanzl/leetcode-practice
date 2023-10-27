"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个 正 整数 k 。
 * 你可以对数组执行以下操作 任意次 ：
 * 选择两个互不相同的下标 i 和 j ，同时 将 nums[i] 更新为 (nums[i] AND nums[j]) 且将 nums[j] 更新为 (nums[i] OR nums[j]) ，OR 表示按位 或 运算，AND 表示按位 与 运算。
 * 你需要从最终的数组里选择 k 个元素，并 计算它们的 平方 之和。
 * 请你返回你可以得到的 最大 平方和。
 * 由于答案可能会很大，将答案对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/apply-operations-on-array-to-maximize-sum-of-squares/
"""
from typing import List


class Solution:

    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        cnt = [0] * 32
        for num in nums:
            for i in range(32):
                cnt[i] += (num >> i) & 1
        ans = 0
        for i in range(k):
            v = 0
            for j in range(32):
                if cnt[j] > i:
                    v += (1 << j)
            ans = (ans + v * v) % MOD
        return ans


if __name__ == '__main__':
    # 24051
    print(Solution().maxSum([25, 52, 75, 65], 4))
    # 261
    print(Solution().maxSum([2, 6, 5, 8], k=2))
    # 90
    print(Solution().maxSum([4, 5, 4, 7], k=3))
