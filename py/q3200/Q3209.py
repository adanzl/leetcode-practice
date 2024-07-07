"""
 * 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中有多少个 子数组 满足：子数组中所有元素按位 AND 的结果为 k 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i], k <= 10^9
 * 链接：https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/
"""
from typing import List


class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = 30
        r_zero, l_one = [-1] * N, [-1] * N
        ans = 0
        for i, num in enumerate(nums):
            ll, rr = 0, i
            for ii in range(N):
                if (1 << ii) & num:  # num ii th bit is 1
                    if l_one[ii] == -1:
                        l_one[ii] = i
                else:
                    l_one[ii] = -1
                    r_zero[ii] = i
                if (1 << ii) & k:  # k ii th bit is 1
                    if l_one[ii] != -1:
                        ll = max(ll, l_one[ii])
                    else:
                        ll = i + 1
                else:
                    if r_zero[ii] != -1:
                        rr = min(rr, r_zero[ii])
                    else:
                        rr = -0x3c3c3c3c3c3c3c3c
            if ll <= rr:
                ans += rr - ll + 1
        return ans


if __name__ == '__main__':
    # 11
    print(Solution().countSubarrays([2, 1, 2, 4, 0], 0))
    # 2
    print(Solution().countSubarrays([1, 2, 3], k=2))
    # 6
    print(Solution().countSubarrays([1, 1, 1], k=1))
    # 1
    print(Solution().countSubarrays([0, 0, 4, 6, 2], 6))
    # 3
    print(Solution().countSubarrays([1, 1, 2], k=1))
