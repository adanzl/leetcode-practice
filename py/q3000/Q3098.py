"""
 * 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
 * 一个子序列的 能量 定义为子序列中 任意 两个元素的差值绝对值的 最小值 。
 * 请你返回 nums 中长度 等于 k 的 所有 子序列的 能量和 。
 * 由于答案可能会很大，将答案对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、2 <= n == nums.length <= 50
 * 2、-10^8 <= nums[i] <= 10^8 
 * 3、2 <= k <= n
 * 链接：https://leetcode.cn/problems/find-the-sum-of-subsequence-powers/
"""
from functools import cache
from typing import Counter, List


class Solution:

    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        '''
        dp[i][j] = Counter()
        到第i位，已选j个数，且i是最后一个数
        Counter:
            最小差值为key有value种情况
        '''
        dp = [[Counter() for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1][int(1e9)] = 1
            for j in range(2, k + 1):
                for li in range(i):
                    for d, t in dp[li][j - 1].items():
                        nd = min(d, nums[i] - nums[li])
                        dp[i][j][nd] += t
        ans = 0
        for i in range(n):
            for v, c in dp[i][k].items():
                ans = (ans + v * c) % (10**9 + 7)
        # 复杂度 50*50*50*250
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().sumOfPowers([-13, 9, -16, -12], 3))
    # 0
    print(Solution().sumOfPowers([2, 2], k=2))
    # 4
    print(Solution().sumOfPowers([1, 2, 3, 4], k=3))
    # 10
    print(Solution().sumOfPowers([4, 3, -1], k=2))
