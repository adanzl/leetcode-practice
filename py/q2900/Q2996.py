"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 如果一个前缀 nums[0..i] 满足对于 1 <= j <= i 的所有元素都有 nums[j] = nums[j - 1] + 1 ，那么我们称这个前缀是一个 顺序前缀 。
 * 特殊情况是，只包含 nums[0] 的前缀也是一个 顺序前缀 。
 * 请你返回 nums 中没有出现过的 最小 整数 x ，满足 x 大于等于 最长 顺序前缀的和。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
"""
from typing import List


class Solution:

    def missingInteger(self, nums: List[int]) -> int:
        mx_len = 1
        mx_idx = 0
        pre = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - pre == 1:
                mx_len += 1
            else:
                break
            pre = nums[i]
        ss = set(nums)
        ans = sum(nums[mx_idx:mx_idx + mx_len])
        while ans in ss:
            ans += 1

        return ans


if __name__ == '__main__':
    # 6
    print(Solution().missingInteger([1, 2, 3, 2, 5]))
    # 47
    print(Solution().missingInteger([46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]))
    # 15
    print(Solution().missingInteger([3, 4, 5, 1, 12, 14, 13]))
    #
    # print(Solution().missingInteger())
