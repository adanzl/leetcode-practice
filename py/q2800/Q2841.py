"""
 * 给你一个整数数组 nums 和两个正整数 m 和 k 。
 * 请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
 * 如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
 * 子数组指的是一个数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 2 * 10^4
 * 2、1 <= m <= k <= nums.length
 * 3、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
"""
from collections import Counter
from typing import List


class Solution:

    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter()
        unique = 0
        ans = 0
        sm = 0
        for i, v in enumerate(nums):
            if cnt[v] == 0:
                unique += 1
            cnt[v] += 1
            sm += v
            if i >= k:
                o = nums[i-k]
                sm -= o
                if cnt[o] == 1:
                    unique -= 1
                if cnt[o] > 0:
                    cnt[o] -= 1
            if unique >= m:
                ans = max(ans, sm)
        return ans


if __name__ == '__main__':
    # 18
    print(Solution().maxSum([2, 6, 7, 3, 1, 7], m=3, k=4))
    # 23
    print(Solution().maxSum([5, 9, 9, 2, 4, 5, 4], m=1, k=3))
    # 0
    print(Solution().maxSum([1, 2, 1, 2, 1, 2, 1], m=3, k=3))
