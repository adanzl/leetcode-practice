"""
 * 给你一个整数数组 nums 和一个 正整数 k 。
 * 请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
 * 子数组是数组中的一个连续元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^6
 * 3、1 <= k <= 10^5
 * 链接：https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/
"""
from typing import List


class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        left, right = 0, 0
        ans = 0
        arr = []
        for i, num in enumerate(nums):
            if num == mx:
                arr.append(i)
            if len(arr) >= k:
                ans += arr[-k] + 1
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().countSubarrays([1, 3, 2, 3, 3], k=2))
    # 0
    print(Solution().countSubarrays([1, 4, 2, 1], k=3))
