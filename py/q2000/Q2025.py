"""
 * 给你一个下标从 0 开始且长度为 n 的整数数组 nums 。
 * 分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目：
 * 1、1 <= pivot < n
 * 2、nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
 * 同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。
 * 请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。
 * 提示：
 * 1、n == nums.length
 * 2、2 <= n <= 10^5
 * 3、-10^5 <= k, nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-number-of-ways-to-partition-an-array/
"""

from itertools import accumulate
from typing import Counter, List

#
# @lc app=leetcode.cn id=2025 lang=python3
#
# [2025] 分割数组的最多方案数
#


# @lc code=start
class Solution:

    def waysToPartition(self, nums: List[int], k: int) -> int:
        pre_sum = [0] + list(accumulate(nums))
        cnt0, cnt1 = Counter(), Counter()
        for i in range(len(nums) - 1, 0, -1):
            d0 = pre_sum[i]
            d1 = pre_sum[-1] - pre_sum[i]
            cnt1[d1 - d0] += 1
        ans = cnt1[0]
        for i in range(1, len(pre_sum)):
            d = pre_sum[-1] - pre_sum[i] - pre_sum[i]
            dk = k - nums[i - 1]
            ans = max(ans, cnt0[-dk] + cnt1[dk])
            cnt0[d] += 1
            cnt1[d] -= 1

        return ans


# @lc code=end

if __name__ == '__main__':
    # 33
    print(Solution().waysToPartition(
        [30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
    # 1
    print(Solution().waysToPartition([2, -1, 2], k=3))
    # 2
    print(Solution().waysToPartition([0, 0, 0], k=1))
    # 4
    print(Solution().waysToPartition([22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], k=-33))
