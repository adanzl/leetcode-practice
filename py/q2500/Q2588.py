"""
 * 给你一个下标从 0 开始的整数数组nums 。每次操作中，你可以：
 * 1、选择两个满足 0 <= i, j < nums.length 的不同下标 i 和 j 。
 * 2、选择一个非负整数 k ，满足 nums[i] 和 nums[j] 在二进制下的第 k 位（下标编号从 0 开始）是 1 。
 * 3、将 nums[i] 和 nums[j] 都减去 2k 。
 * 如果一个子数组内执行上述操作若干次后，该子数组可以变成一个全为 0 的数组，那么我们称它是一个 美丽 的子数组。
 * 请你返回数组 nums 中 美丽子数组 的数目。
 * 子数组是一个数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/
"""
from collections import Counter
from itertools import accumulate
from operator import xor
from typing import List


class Solution:

    def beautifulSubarrays(self, nums: List[int]) -> int:
        s = list(accumulate(nums, xor, initial=0))  # 前缀异或
        ans, cnt = 0, Counter()
        for x in s:
            # 先计入答案再统计个数，如果反过来的话，就相当于把空子数组也计入答案了
            ans += cnt[x]
            cnt[x] += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().beautifulSubarrays([4, 3, 1, 2, 4]))
    # 1
    print(Solution().beautifulSubarrays([0]))
    # 3
    print(Solution().beautifulSubarrays([0, 0]))
    # 0
    print(Solution().beautifulSubarrays([1, 10, 4]))
