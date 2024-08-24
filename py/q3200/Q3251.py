"""
 * 给你一个长度为 n 的 正 整数数组 nums 。
 * 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对：
 * 1、两个数组的长度都是 n 。
 * 2、arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。
 * 3、arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。
 * 4、对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。
 * 请你返回所有 单调 数组对的数目。
 * 由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= n == nums.length <= 2000
 * 2、1 <= nums[i] <= 1000
 * 链接：https://leetcode.cn/problems/find-the-count-of-monotonic-pairs-ii/
"""
import bisect
from typing import List


class Solution:

    def countOfPairs(self, nums: List[int]) -> int:
        MX = 0x3c3c3c3c3c3c3c3c
        MOD = 10**9 + 7
        dp = [-MX for _ in range(1001)]
        pre_sum = [1 for i in range(1005)]
        pre_sum[0] = 0
        for num in nums:
            n_dp = [0 for _ in range(1005)]
            n_pre_sum = [0]
            for v0 in range(num + 1):
                v1 = num - v0
                ii = bisect.bisect_right(dp, -v1, hi=v0 + 1)
                val = pre_sum[ii]
                n_dp[v0] = -v1
                n_pre_sum.append((n_pre_sum[-1] + val) % MOD)
            for _ in range(num + 1, 1005):
                n_pre_sum.append(n_pre_sum[-1])
            dp = n_dp
            pre_sum = n_pre_sum
        return pre_sum[-1]


if __name__ == '__main__':
    # 4
    print(Solution().countOfPairs([2, 3, 2]))
    # 126
    print(Solution().countOfPairs([5, 5, 5, 5]))
