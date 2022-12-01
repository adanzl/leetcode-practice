"""
 * 给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的维度，且一开始全部为 0 。
 * 请你返回从 initial 得到  target 的最少操作次数，每次操作需遵循以下规则：
 * 在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。
 * 答案保证在 32 位有符号整数以内。
 * 提示：
 * 1、1 <= target.length <= 10^5
 * 2、1 <= target[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
"""
from itertools import pairwise
from typing import List


class Solution:

    # 差分数组 区间增加或减少
    def minNumberOperations1(self, target: List[int]) -> int:
        ans = 0
        for a, b in pairwise([0] + target):
            if a <= b: ans += b - a
        return ans

    # 单调栈
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        s = []
        for t in target:
            if s and s[-1] >= t: ans += s.pop() - t
            while s and s[-1] >= t:
                s.pop()
            s.append(t)
        return ans + s[-1]


if __name__ == '__main__':
    # 8
    print(Solution().minNumberOperations([3, 4, 2, 5, 6]))
    # 3
    print(Solution().minNumberOperations([1, 2, 3, 2, 1]))
    # 4
    print(Solution().minNumberOperations([3, 1, 1, 2]))
    # 7
    print(Solution().minNumberOperations([3, 1, 5, 4, 2]))
    # 1
    print(Solution().minNumberOperations([1, 1, 1, 1]))
