"""
 * 给你一个下标从 0 开始的整数数组 nums 。你需要将 nums 重新排列成一个新的数组 perm 。
 * 定义 nums 的 伟大值 为满足 0 <= i < nums.length 且 perm[i] > nums[i] 的下标数目。
 * 请你返回重新排列 nums 后的 最大 伟大值。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximize-greatness-of-an-array/
"""
from bisect import bisect_left
from typing import List


class Solution:

    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans, lo, n = 0, 0, len(nums)
        for num in nums:
            idx = bisect_left(nums, num + 1, lo)
            if idx == n: break
            ans += 1
            lo = idx + 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maximizeGreatness([1, 3, 5, 2, 1, 3, 1]))
    # 6
    print(Solution().maximizeGreatness([42, 8, 75, 28, 35, 21, 13, 21]))
    # 3
    print(Solution().maximizeGreatness([1, 2, 3, 4]))
