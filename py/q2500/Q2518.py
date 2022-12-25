"""
 * 给你一个正整数数组 nums 和一个整数 k 。
 * 分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。
 * 返回 不同 的好分区的数目。由于答案可能很大，请返回对 10^9 + 7 取余 后的结果。
 * 如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。
 * 提示：
 * 1、1 <= nums.length, k <= 1000
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/number-of-great-partitions/
"""
from typing import List


class Solution:

    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if sum(nums) < k * 2: return 0
        dp = [0] * (k)
        dp[0] = 1
        for i in range(n):
            for j in range(k - 1, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return ((1 << n) - sum(dp) * 2) % MOD


if __name__ == '__main__':
    # 6
    print(Solution().countPartitions([1, 2, 3, 4], 4))
    # 0
    print(Solution().countPartitions([3, 3, 3], 4))
    # 2
    print(Solution().countPartitions([6, 6], 2))
