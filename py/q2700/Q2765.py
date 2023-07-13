"""
 * 给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子序列 ：
 * 1、m 大于 1 。
 * 2、s1 = s0 + 1 。
 * 3、下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
 * 请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。
 * 子数组是一个数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/longest-alternating-subarray/
"""
from typing import List


class Solution:

    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        p, m = [1] * n, [1] * n
        ans = -1
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:
                m[i] = p[i - 1] + 1
                ans = max(ans, m[i])
            elif nums[i] - nums[i - 1] == -1 and m[i - 1] != 1:
                p[i] = m[i - 1] + 1
                ans = max(ans, p[i])
        return ans


if __name__ == '__main__':
    # -1
    print(Solution().alternatingSubarray([14, 30, 29, 49, 3, 23, 44, 21, 26, 52]))
    # -1
    print(Solution().alternatingSubarray([21, 9, 5]))
    # 2
    print(Solution().alternatingSubarray([4, 5, 6]))
    # 4
    print(Solution().alternatingSubarray([2, 3, 4, 3, 4]))
