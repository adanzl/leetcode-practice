"""
 * 给你一个下标从 0 开始的整数数组 nums ，它包含 3 * n 个元素。
 * 你可以从 nums 中删除 恰好 n 个元素，剩下的 2 * n 个元素将会被分成两个 相同大小 的部分。
 * 1、前面 n 个元素属于第一部分，它们的和记为 sum_first 。
 * 2、后面 n 个元素属于第二部分，它们的和记为 sum_second 。
 * 两部分和的 差值 记为 sum_first - sum_second 。
 * 1、比方说，sum_first = 3 且 sum_second = 2 ，它们的差值为 1 。
 * 2、再比方，sum_first = 2 且 sum_second = 3 ，它们的差值为 -1 。
 * 请你返回删除 n 个元素之后，剩下两部分和的 差值的最小值 是多少。
 * 提示：
 * 1、nums.length == 3 * n
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=2163 lang=python3
#
# [2163] 删除元素后和的最小差值
#


# @lc code=start
class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        f = [0] * len(nums)
        h = []
        for i in range(n * 2):
            f[i] = (f[i - 1] if i else 0) + nums[i]
            heappush(h, -nums[i])
            if len(h) > n:
                f[i] += heappop(h)
        ans = 10**10
        lst = 0
        h = []
        for i in range(n * 3 - 1, n - 1, -1):
            lst += nums[i]
            heappush(h, nums[i])
            if len(h) > n:
                lst -= heappop(h)
            if i <= n * 2:
                ans = min(ans, f[i - 1] - lst)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().minimumDifference([7, 9, 5, 8, 1, 3]))
    # -1
    print(Solution().minimumDifference([3, 1, 2]))
