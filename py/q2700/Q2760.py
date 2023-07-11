"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 threshold 。
 * 请你从 nums 的子数组中找出以下标 l 开头、下标 r 结尾 (0 <= l <= r < nums.length) 且满足以下条件的 最长子数组 ：
 * 1、nums[l] % 2 == 0
 * 2、对于范围 [l, r - 1] 内的所有下标 i ，nums[i] % 2 != nums[i + 1] % 2
 * 3、对于范围 [l, r] 内的所有下标 i ，nums[i] <= threshold
 * 以整数形式返回满足题目要求的最长子数组的长度。
 * 注意：子数组 是数组中的一个连续非空元素序列。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、1 <= threshold <= 100
 * 链接：https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/
"""
from typing import List


class Solution:

    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        ln = 0

        for num in nums:
            if num <= threshold and ln % 2 == num % 2:
                ln += 1
            else:
                ans = max(ans, ln)
                ln = 1 if num % 2 == 0 and num <= threshold else 0
        return max(ans, ln)


if __name__ == '__main__':
    # 0
    print(Solution().longestAlternatingSubarray([4], threshold=1))
    # 2
    print(Solution().longestAlternatingSubarray([4, 10, 3], threshold=10))
    # 3
    print(Solution().longestAlternatingSubarray([3, 2, 5, 4], threshold=5))
    # 1
    print(Solution().longestAlternatingSubarray([1, 2], threshold=2))
    # 3
    print(Solution().longestAlternatingSubarray([2, 3, 4, 5], threshold=4))
