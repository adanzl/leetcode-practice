"""
 * 给你一个二进制数组 nums 。
 * 你可以对数组执行以下操作 任意 次（也可以 0 次）：
 * 选择数组中 任意 一个下标 i ，并将从下标 i 开始一直到数组末尾 所有 元素 反转 。
 * 反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
 * 请你返回将 nums 中所有元素变为 1 的 最少 操作次数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 1
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans, f1, f0 = 0, 0, 0
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                f1 = 1
                if f0:
                    ans += 1
                f0 = 0
            elif nums[i] == 0:
                if f1:
                    ans += 1
                f1 = 0
                f0 = 1
        return ans + f0


if __name__ == '__main__':
    # 4
    print(Solution().minOperations([0, 1, 1, 0, 1]))
    # 1
    print(Solution().minOperations([1, 0, 0, 0]))
