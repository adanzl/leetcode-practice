"""
 * 给你一个下标从 0 开始的整数数组 nums 。nums 的一个子数组如果满足以下条件，那么它是 不间断 的：
 * i，i + 1 ，...，j  表示子数组中的下标。对于所有满足 i <= i1, i2 <= j 的下标对，都有 0 <= |nums[i1] - nums[i2]| <= 2 。
 * 请你返回 不间断 子数组的总数目。
 * 子数组是一个数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/continuous-subarrays/
"""
from collections import Counter

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = left = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            while max(cnt) - min(cnt) > 2:
                y = nums[left]
                cnt[y] -= 1
                if cnt[y] == 0: del cnt[y]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().continuousSubarrays([5, 4, 2, 4]))
    # 49930000
    print(Solution().continuousSubarrays(TestCase('res\\q2700\\Q3_1').getDataIntArray()))
    # 6
    print(Solution().continuousSubarrays([1, 2, 3]))
