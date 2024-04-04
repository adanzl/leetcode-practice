"""
 * 给你一个 非负 整数数组 nums 和一个整数 k 。
 * 如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。
 * 请你返回 nums 中 最短特别非空 子数组 的长度，如果特别子数组不存在，那么返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、0 <= nums[i] <= 50
 * 3、0 <= k < 64
 * 链接：https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/
"""
from typing import List


class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LIMIT = 0x3c3c3c3c3c3c
        ans = LIMIT
        for i in range(n):
            v = nums[i]
            j = i + 1
            while v < k and j < n:
                v |= nums[j]
                j += 1
            if v >= k:
                ans = min(ans, j - i)
        return ans if ans != LIMIT else -1


if __name__ == '__main__':
    # 1
    print(Solution().minimumSubarrayLength([2, 24, 32, 1], 11))
    # -1
    print(Solution().minimumSubarrayLength([1, 12, 2, 5], 43))
    # 1
    print(Solution().minimumSubarrayLength([1, 2, 3], k=3))
    # 3
    print(Solution().minimumSubarrayLength([2, 1, 8], k=10))
    # 1
    print(Solution().minimumSubarrayLength([1, 2], k=0))
