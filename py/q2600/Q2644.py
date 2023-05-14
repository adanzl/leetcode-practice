"""
 * 给你两个下标从 0 开始的整数数组 nums 和 divisors 。
 * divisors[i] 的 可整除性得分 等于满足 nums[j] 能被 divisors[i] 整除的下标 j 的数量。
 * 返回 可整除性得分 最大的整数 divisors[i] 。如果有多个整数具有最大得分，则返回数值最小的一个。
 * 提示：
 * 1、1 <= nums.length, divisors.length <= 1000
 * 2、1 <= nums[i], divisors[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-maximum-divisibility-score/
"""
from typing import List


class Solution:

    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans, s = 10**9, -1
        for d in divisors:
            sm = 0
            for num in nums:
                if num % d == 0:
                    sm += 1
            if sm > s:
                s, ans = sm, d
            elif sm == s:
                ans = min(ans, d)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().maxDivScore([4, 7, 9, 3, 9], divisors=[5, 2, 3]))
    # 5
    print(Solution().maxDivScore([20, 14, 21, 10], divisors=[5, 7, 5]))
    # 10
    print(Solution().maxDivScore([12], divisors=[10, 16]))
