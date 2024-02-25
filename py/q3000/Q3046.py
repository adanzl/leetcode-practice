"""
 * 给你一个长度为 偶数 的整数数组 nums 。你需要将这个数组分割成 nums1 和 nums2 两部分，要求：
 * 1、nums1.length == nums2.length == nums.length / 2 。
 * 2、nums1 应包含 互不相同 的元素。
 * 3、nums2也应包含 互不相同 的元素。
 * 如果能够分割数组就返回 true ，否则返回 false 。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、nums.length % 2 == 0
 * 3、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/split-the-array/
"""
from typing import Counter, List


class Solution:

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return max(Counter(nums).values()) <= 2


if __name__ == '__main__':
    # True
    print(Solution().isPossibleToSplit([1, 1, 2, 2, 3, 4]))
    # False
    print(Solution().isPossibleToSplit([1, 1, 1, 1]))
