"""
 * 给你一个下标从 0 开始的整数数组 nums ，以及整数 modulo 和整数 k 。
 * 请你找出并统计数组中 趣味子数组 的数目。
 * 如果 子数组 nums[l..r] 满足下述条件，则称其为 趣味子数组 ：
 * 在范围 [l, r] 内，设 cnt 为满足 nums[i] % modulo == k 的索引 i 的数量。并且 cnt % modulo == k 。
 * 以整数形式表示并返回趣味子数组的数目。
 * 注意：子数组是数组中的一个连续非空的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5 
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= modulo <= 10^9
 * 4、0 <= k < modulo
 * 链接：https://leetcode.cn/problems/count-of-interesting-subarrays/
"""
from collections import Counter
from typing import List


class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        ans = 0
        cnt = Counter({0: 1})
        for i, num in enumerate(nums):
            cur = 1 if num % modulo == k else 0
            v = pre_sum[i + 1] = pre_sum[i] + cur
            vr = v % modulo
            pr = vr - k
            if pr < 0: pr += modulo
            ans += cnt[pr]
            cnt[vr] += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countInterestingSubarrays([3, 2, 4], modulo=2, k=1))
    # 2
    print(Solution().countInterestingSubarrays([3, 1, 9, 6], modulo=3, k=0))
    #
    # print(Solution().countInterestingSubarrays())