"""
 * 给你两个长度相同的正整数数组 nums 和 target。
 * 在一次操作中，你可以选择 nums 的任何 子数组，并将该子数组内的每个元素的值增加或减少 1。
 * 返回使 nums 数组变为 target 数组所需的 最少 操作次数。
 * 提示：
 * 1、1 <= nums.length == target.length <= 10^5
 * 2、1 <= nums[i], target[i] <= 10^8
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-array-equal-to-target/
"""
from itertools import pairwise
from typing import List


class Solution:

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        dd = target[0] - nums[0]
        ans = abs(dd)
        for (a, b), (c, d) in pairwise(zip(nums, target)):
            # 构建查分数组，求差分数组的最优形成方式为答案
            val = (d - c) - (b - a)
            if val > 0:
                ans += val if dd >= 0 else max(val + dd, 0)
            else:
                ans -= val if dd <= 0 else min(val + dd, 0)
            dd += val
        return ans

    def minimumOperations1(self, nums: List[int], target: List[int]) -> int:
        ans = 0
        pre = 0
        q = []
        for v in [a - b for a, b in zip(nums, target)]:
            if v > 0:
                if pre <= 0: q = []
                f = False
                while q and q[-1] > v:
                    q.pop()
                    f = True
                if not f:
                    ans += v - (q[-1] if q else 0)
                q.append(v)
            if v < 0:
                if pre >= 0: q = []
                f = False
                while q and q[-1] < v:
                    q.pop()
                    f = True
                if not f:
                    ans += (q[-1] if q else 0) - v
                q.append(v)
            pre = v
        return ans


if __name__ == '__main__':
    # 5
    print(Solution().minimumOperations([1, 3, 2], target=[2, 1, 4]))
    # 20
    print(Solution().minimumOperations([9, 2, 6, 10, 4, 8, 3, 4, 2, 3], [9, 5, 5, 1, 7, 9, 8, 7, 6, 5]))
    # 2
    print(Solution().minimumOperations([3, 5, 1, 2], target=[4, 6, 2, 4]))
