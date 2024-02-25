"""
 * 给你两个下标从 1 开始的整数数组 nums 和 changeIndices ，数组的长度分别为 n 和 m 。
 * 一开始，nums 中所有下标都是未标记的，你的任务是标记 nums 中 所有 下标。
 * 从第 1 秒到第 m 秒（包括 第 m 秒），对于每一秒 s ，你可以执行以下操作 之一 ：
 * 1、选择范围 [1, n] 中的一个下标 i ，并且将 nums[i] 减少 1 。
 * 2、如果 nums[changeIndices[s]] 等于 0 ，标记 下标 changeIndices[s] 。
 * 3、什么也不做。
 * 请你返回范围 [1, m] 中的一个整数，表示最优操作下，标记 nums 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 -1 。
 * 提示：
 * 1、1 <= n == nums.length <= 2000
 * 2、0 <= nums[i] <= 10^9
 * 3、1 <= m == changeIndices.length <= 2000
 * 4、1 <= changeIndices[i] <= n
 * 链接：https://leetcode.cn/problems/earliest-second-to-mark-indices-i/
"""
from typing import List


class Solution:

    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)
        ans = -1

        def func(size):
            d = {}
            for i in range(size):
                v = changeIndices[i]
                d[v] = max(i + 1, d.get(v, 0))
            if len(d) < n:
                return False
            cnt = 0
            for t, v in sorted([[t, v] for v, t in d.items()]):
                cnt += nums[v - 1] + 1
                if cnt > t:
                    return False
            return True

        l, r = 0, m
        while l <= r:
            mid = (l + r) // 2
            if func(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().earliestSecondToMarkIndices([1, 3], changeIndices=[1, 1, 1, 2, 1, 1, 1]))
    # 8
    print(Solution().earliestSecondToMarkIndices([2, 2, 0], changeIndices=[2, 2, 2, 2, 3, 2, 2, 1]))
    # -1
    print(Solution().earliestSecondToMarkIndices([0, 1], changeIndices=[2, 2, 2]))
