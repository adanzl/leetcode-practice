"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。
 * 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
 * 请你返回你能得到的 最大得分 。
 * 提示：
 * 1、1 <= nums.length, k <= 10^5
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/jump-game-vi/
"""
from typing import List, Deque


class Solution:

    def maxResult(self, nums: List[int], k: int) -> int:
        q = Deque()
        n = len(nums)
        dp = [0] * n
        for i, num in enumerate(nums):
            while q and i - q[0] > k:
                q.popleft()
            dp[i] = num + (dp[q[0]] if q else 0)
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return dp[-1]


if __name__ == '__main__':
    # 7
    print(Solution().maxResult([1, -1, -2, 4, -7, 3], 2))
    # 17
    print(Solution().maxResult([10, -5, -2, 4, 0, 3], 3))
    # 0
    print(Solution().maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2))
