"""
 * 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 nums 的 子数组 中满足 元素最小公倍数为 k 的子数组数目。
 * 子数组 是数组中一个连续非空的元素序列。
 * 数组的最小公倍数 是可被所有数组元素整除的最小正整数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i], k <= 1000
 * 链接：https://leetcode.cn/problems/number-of-subarrays-with-lcm-equal-to-k/
"""
from collections import Counter
from math import lcm
from typing import List


class Solution:

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = Counter({1: 0})
        ans = 0
        for i in range(n):
            n_dic = Counter({nums[i]: 1})
            for v, c in dp.items():
                vv = lcm(nums[i], v)
                if vv > k: continue
                n_dic[vv] += c
            dp = n_dic
            ans += n_dic[k]
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().subarrayLCM([3, 6, 2, 7, 1], 6))
    # 0
    print(Solution().subarrayLCM([3], 2))
