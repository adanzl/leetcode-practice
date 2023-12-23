"""
 * 给你一个整数数组 nums 和一个整数 k 。
 * 一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。
 * 如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。
 * 请你返回 nums 中 最长好 子数组的长度。
 * 子数组 指的是一个数组中一段连续非空的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= nums.length
 * 链接：https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/
"""
from collections import Counter
from typing import List


class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()
        ans = 0
        l, r = 0, 0
        while l < n:
            while r < n and cnt[nums[r]] < k:
                cnt[nums[r]] += 1
                r += 1
            ans = max(ans, r - l)
            cnt[nums[l]] -= 1
            l += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().maxSubarrayLength([2, 2, 3], 1))
    # 6
    print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], k=2))
    # 2
    print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], k=1))
    # 4
    print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], k=4))
