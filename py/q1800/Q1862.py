"""
 * 给你一个整数数组 nums ，请你返回所有下标对 0 <= i, j < nums.length 的 floor(nums[i] / nums[j]) 结果之和。
 * 由于答案可能会很大，请你返回答案对10^9 + 7 取余 的结果。
 * 函数 floor() 返回输入数字的整数部分。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/sum-of-floored-pairs/
"""

from typing import List

#
# @lc app=leetcode.cn id=1862 lang=python3
#
# [1862] 向下取整数对和
#


# @lc code=start
class Solution:

    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ans, mx = 0, max(nums)
        cnt = [0] * (mx + 1)
        for num in nums:
            cnt[num] += 1
        pre = [0] * (mx + 1)
        for i in range(1, mx + 1):
            pre[i] = pre[i - 1] + cnt[i]
        # 暴力枚举
        for num in range(1, mx + 1):
            if cnt[num] == 0: continue
            d = 1
            while d * num <= mx:
                ans += cnt[num] * d * (pre[min((d + 1) * num - 1, mx)] - pre[d * num - 1])
                d += 1
            ans %= MOD
        return ans


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().sumOfFlooredPairs([7, 7]))
    # 49
    print(Solution().sumOfFlooredPairs([7, 7, 7, 7, 7, 7, 7]))
    # 10
    print(Solution().sumOfFlooredPairs([2, 5, 9]))
