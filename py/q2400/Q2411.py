"""
 * 给你一个长度为 n 下标从 0 开始的数组 nums ，数组中所有数字均为非负整数。对于 0 到 n - 1 之间的每一个下标 i ，
 * 你需要找出 nums 中一个 最小 非空子数组，它的起始位置为 i （包含这个位置），同时有 最大 的 按位或运算值 。
 * 换言之，令 Bij 表示子数组 nums[i...j] 的按位或运算的结果，你需要找到一个起始位置为 i 的最小子数组，这个子数组的按位或运算的结果等于 max(Bik) ，其中 i <= k <= n - 1 。
 * 一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。
 * 请你返回一个大小为 n 的整数数组 answer，其中 answer[i]是开始位置为 i ，按位或运算结果最大，且 最短 子数组的长度。
 * 子数组 是数组里一段连续非空元素组成的序列。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 10^5
 * 3、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/
"""

from collections import deque
from typing import *


class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        idx = [deque() for _ in range(32)]
        for i, num in enumerate(nums):
            for n in range(32):
                if (1 << n & num) != 0:
                    idx[n].append(i)
        ans = [1] * len(nums)
        for i in range(len(ans)):
            for j in range(32):
                q = idx[j]
                while q and q[0] < i:
                    q.popleft()
                if q:
                    ans[i] = max(ans[i], q[0] - i + 1)
        return ans


if __name__ == '__main__':
    # [3,3,2,2,1]
    print(Solution().smallestSubarrays([1, 0, 2, 1, 3]))
    # [2,1]
    print(Solution().smallestSubarrays([1, 2]))
    # [1]
    print(Solution().smallestSubarrays([0]))
