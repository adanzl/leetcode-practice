"""
 * 给你一个长度为 2 * n 的整数数组。
 * 你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。
 * nums 中每个元素都需要放入两个数组之一。
 * 请你返回 最小 的数组和之差。
 * 提示：
 * 1、1 <= n <= 15
 * 2、nums.length == 2 * n
 * 3、-10^7 <= nums[i] <= 10^7
 * 链接：https://leetcode.cn/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
"""

import bisect
from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=2035 lang=python3
#
# [2035] 将数组分成两个数组并最小化数组和的差
#


# @lc code=start
class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        LIMIT = 0x3c3c3c3c3c3c
        ans, sm = LIMIT, sum(nums)
        target, n = sm // 2, len(nums) // 2
        l_m, r_m = defaultdict(list), defaultdict(list)
        # 数组切割成左右两边，l_m[i]/r_m[i]表示取i个元素时的可能值
        for i in range(1 << n):
            sm_l, sm_r = 0, 0
            for j in range(n):
                if i & (1 << j):
                    sm_l += nums[j]
                    sm_r += nums[n + j]
            bisect.insort(l_m[i.bit_count()], sm_l)
            bisect.insort(r_m[i.bit_count()], sm_r)
        # 枚举左子数组取i个元素，右子数组取n-i个元素
        for i in range(n + 1):
            j = n - i
            for v_l in l_m[i]:
                d = target - v_l
                idx = bisect.bisect_left(r_m[j], d)
                if idx > 0:
                    ans = min(ans, abs(sm - 2 * (v_l + r_m[j][idx - 1])))
                if idx < len(r_m[j]):
                    ans = min(ans, abs(sm - 2 * (v_l + r_m[j][idx])))

        return ans


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().minimumDifference([
        7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283, 5919119,
        3093450, 1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873, 302974, 7656726,
        -2572679, 0, 2121026, -5743797, -8897395, -9699694
    ]))
    # 2
    print(Solution().minimumDifference([3, 9, 7, 3]))
    # 72
    print(Solution().minimumDifference([-36, 36]))
    # 0
    print(Solution().minimumDifference([2, -1, 0, 4, -2, -9]))
