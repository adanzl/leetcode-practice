"""
 * 给定一个整数数组 A，坡是元组 (i, j)，其中  i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
 * 找出 A 中的坡的最大宽度，如果不存在，返回 0 。
 * 提示：
 * 1、2 <= A.length <= 50000
 * 2、0 <= A[i] <= 50000
 * 链接：https://leetcode.cn/problems/maximum-width-ramp/
"""
from typing import List


class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        # 单调栈 把所有可能作为左端点的值都放入栈中
        s = []
        n = len(nums)
        for i, num in enumerate(nums):
            if not s or nums[s[-1]] > num:
                s.append(i)
        ans = 0
        for i in range(n - 1, -1, -1):
            while s and nums[s[-1]] <= nums[i]:
                ans = max(ans, i - s.pop())
            if not s: break
        return ans

    def maxWidthRamp1(self, nums: List[int]) -> int:
        # greedy
        arr = sorted([[num, i] for num, i in zip(nums, range(len(nums)))], key=lambda x: (x[0], x[1]))
        ans, mn = 0, arr[0][1]
        for num, idx in arr:
            ans = max(ans, idx - mn)
            mn = min(mn, idx)
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]))
    # 7
    print(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
