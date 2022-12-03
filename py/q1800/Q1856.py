"""
 * 一个数组的 最小乘积 定义为这个数组中 最小值 乘以 数组的 和 。
 * 比方说，数组 [3,2,5] （最小值是 2）的最小乘积为 2 * (3+2+5) = 2 * 10 = 20 。
 * 给你一个正整数数组 nums ，请你返回 nums 任意 非空子数组 的最小乘积 的 最大值 。由于答案可能很大，请你返回答案对  10^9 + 7 取余 的结果。
 * 请注意，最小乘积的最大值考虑的是取余操作 之前 的结果。题目保证最小乘积的最大值在 不取余 的情况下可以用 64 位有符号整数 保存。
 * 子数组 定义为一个数组的 连续 部分。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^7
 * 链接：https://leetcode.cn/problems/maximum-subarray-min-product/
"""
from itertools import accumulate
from typing import List


class Solution:

    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        pre_sum = [0] + list(accumulate(nums))
        r = [n] * n
        s = []
        ans = 0
        for i in range(n - 1, -1, -1):
            while s and nums[s[-1]] >= nums[i]:
                s.pop()
            if s: r[i] = s[-1]
            s.append(i)
        s.clear()
        for i in range(n):
            while s and nums[s[-1]] >= nums[i]:
                s.pop()
            l = s[-1] if s else -1
            ans = max(ans, nums[i] * (pre_sum[r[i]] - pre_sum[l + 1]))
            s.append(i)
        return ans % MOD


if __name__ == '__main__':
    # 14
    print(Solution().maxSumMinProduct([1, 2, 3, 2]))
    # 18
    print(Solution().maxSumMinProduct([2, 3, 3, 1, 2]))
    # 60
    print(Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]))
