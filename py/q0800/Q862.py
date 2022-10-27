"""
 * 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
 * 子数组 是数组中 连续 的一部分。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、-10^5 <= nums[i] <= 10^5
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
"""
from itertools import accumulate
from typing import Deque, List


class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = n + 1
        pre_sum = [0] + list(accumulate(nums))
        q = Deque()
        for i, curSum in enumerate(pre_sum):
            while q and curSum - pre_sum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and pre_sum[q[-1]] >= curSum:
                q.pop()
            q.append(i)
        return ans if ans < n + 1 else -1


if __name__ == '__main__':
    # 3
    print(Solution().shortestSubarray([2, -1, 2], 3))
    # 1
    print(Solution().shortestSubarray([1], 1))
    # -1
    print(Solution().shortestSubarray([1, 2], 4))
