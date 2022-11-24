"""
 * 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。
 * 数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。
 * 提示：
 * 1、1 <= k <= nums.length <= 10^5
 * 2、-10^4 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/constrained-subsequence-sum/
"""
from typing import List, Deque


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n  # 以第i项为最后一项的最大子序列的和
        q = Deque()  # 单调队列，保存递减dp索引
        for i in range(n):
            dp[i] = nums[i]
            # 如果最大的和与当前元素距离大于k则抛弃
            while q and q[0] < i - k:
                q.popleft()
            if q: dp[i] = max(dp[i], dp[q[0]] + nums[i])
            while q and dp[q[-1]] < dp[i]:
                q.pop()
            q.append(i)
        return max(dp)


if __name__ == '__main__':
    # 23
    print(Solution().constrainedSubsetSum([10, -2, -10, -5, 20], 2))
    # 37
    print(Solution().constrainedSubsetSum([10, 2, -10, 5, 20], 2))
    # -1
    print(Solution().constrainedSubsetSum([-1, -2, -3], 1))
