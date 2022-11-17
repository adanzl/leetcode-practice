"""
 * 给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：
 * 1、i + x ，其中 i + x < arr.length 且 0 < x <= d 。
 * 2、i - x ，其中 i - x >= 0 且 0 < x <= d 。
 * 除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。
 * 你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。
 * 请注意，任何时刻你都不能跳到数组的外面。
 * 提示：
 * 1、1 <= arr.length <= 1000
 * 2、1 <= arr[i] <= 10^5
 * 3、1 <= d <= arr.length
 * 链接：https://leetcode.cn/problems/jump-game-v/
"""
from functools import cache
from typing import List


class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        @cache
        def f(idx):
            ret = 0
            for i in range(idx - 1, max(0, idx - d) - 1, -1):  # left
                if arr[i] >= arr[idx]: break
                ret = max(ret, f(i))
            for i in range(idx + 1, min(n, idx + d + 1)):  # right
                if arr[i] >= arr[idx]: break
                ret = max(ret, f(i))
            return ret + 1

        return max([f(i) for i in range(n)])


if __name__ == '__main__':
    # 7
    print(Solution().maxJumps([7, 6, 5, 4, 3, 2, 1], 1))
    # 4
    print(Solution().maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
    # 1
    print(Solution().maxJumps([3, 3, 3, 3, 3], 3))
    # 2
    print(Solution().maxJumps([7, 1, 7, 1, 7, 1], 2))
    # 1
    print(Solution().maxJumps([66], 1))
