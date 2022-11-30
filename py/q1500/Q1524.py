"""
 * 给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。
 * 由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 100
 * 链接：https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/
"""
from typing import List


class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        dp = [0, 0]  # odd even
        for num in arr:
            if num & 1:  # odd
                dp = [dp[1] + 1, dp[0]]
            else:
                dp = [dp[0], dp[1] + 1]
            ans += dp[0]
        return ans % (10**9 + 7)


if __name__ == '__main__':
    # 0
    print(Solution().numOfSubarrays([2, 4, 6]))
    # 4
    print(Solution().numOfSubarrays([1, 3, 5]))
    # 16
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
    # 4
    print(Solution().numOfSubarrays([100, 100, 99, 99]))
    # 1
    print(Solution().numOfSubarrays([7]))
