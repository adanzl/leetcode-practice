"""
 * 给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。
 * 你可以执行下面操作 任意 次：
 * 将 nums 中 任意 元素增加或者减小 1 。
 * 对第 i 个元素执行一次操作的开销是 cost[i] 。
 * 请你返回使 nums 中所有元素 相等 的 最少 总开销。
 * 提示：
 * 1、n == nums.length == cost.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i], cost[i] <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-cost-to-make-array-equal/
"""
from typing import List


class Solution:

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        arr = sorted(zip(nums, cost))
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + arr[i][1]
        ans = 0
        for i in range(1, n):
            ans += arr[i][1] * (arr[i][0] - arr[0][0])
        pre = ans
        for i in range(1, n):
            pre += pre_sum[i] * (arr[i][0] - arr[i - 1][0])
            pre -= (pre_sum[-1] - pre_sum[i]) * (arr[i][0] - arr[i - 1][0])
            ans = min(ans, pre)
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().minCost([1, 3, 5, 2], [2, 3, 1, 14]))
    # 0
    print(Solution().minCost([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]))
