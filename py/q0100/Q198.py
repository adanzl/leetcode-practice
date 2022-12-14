"""
 * 你是一个专业的小偷，计划偷窃沿街的房屋。
 * 每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
 * 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、0 <= nums[i] <= 400
 * 链接：https://leetcode.cn/problems/house-robber/
"""
from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]  # choose last or not
        for num in nums:
            dp = [max(dp), dp[0] + num]
        return max(dp)


if __name__ == '__main__':
    # 4
    print(Solution().rob([1, 2, 3, 1]))
    # 12
    print(Solution().rob([2, 7, 9, 3, 1]))
