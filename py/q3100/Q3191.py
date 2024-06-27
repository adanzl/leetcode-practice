"""
 * 给你一个二进制数组 nums 。
 * 你可以对数组执行以下操作 任意 次（也可以 0 次）：
 * 选择数组中 任意连续 3 个元素，并将它们 全部反转 。
 * 反转 一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。
 * 请你返回将 nums 中所有元素变为 1 的 最少 操作次数。如果无法全部变成 1 ，返回 -1 。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 1
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        LIMIT = 0x3c3c3c3c3c3c
        ans = LIMIT
        n = len(nums)
        nn = nums[:]
        fl = [0] + [LIMIT] * n
        for ii in range(n - 2):
            if nn[ii] == 0:
                fl[ii + 1] = min(fl[ii + 1], fl[ii] + 1)
                for j in range(ii, min(n, ii + 3)):
                    nn[j] = 1 ^ nn[j]
            else:
                fl[ii + 1] = min(fl[ii + 1], fl[ii])
        for ii in range(n - 2, n):
            if nn[ii] == 0: break
        else:
            ans = fl[n - 2]

        return ans if ans != LIMIT else -1


if __name__ == '__main__':
    # 3
    print(Solution().minOperations([0, 1, 1, 1, 0, 0]))
    # -1
    print(Solution().minOperations([1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]))
    # -1
    print(Solution().minOperations([0, 1, 1, 1]))
