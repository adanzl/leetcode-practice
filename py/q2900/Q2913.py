"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 定义 nums 一个子数组的 不同计数 值如下：
 * 令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），
 * 那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。
 * 请你返回 nums 中所有子数组的 不同计数 的 平方 和。
 * 由于答案可能会很大，请你将它对 10^9 + 7 取余 后返回。
 * 子数组指的是一个数组里面一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-i/
"""
from collections import Counter
from typing import List


class Solution:

    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            cnt = Counter()
            for j in range(i, -1, -1):
                cnt[nums[j]] += 1
                ans = (ans + len(cnt.keys())**2) % (10**9 + 7)
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().sumCounts([1, 2, 1]))
    # 3
    print(Solution().sumCounts([1, 1]))
