"""
 * 给你一个由 正 整数组成的数组 nums 。
 * 如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
 * 子数组中 不同 元素的数目等于整个数组不同元素的数目。
 * 返回数组中 完全子数组 的数目。
 * 子数组 是数组中的一个连续非空序列。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 2000
 * 链接：https://leetcode.cn/problems/count-complete-subarrays-in-an-array/
"""
from collections import Counter
from typing import List


class Solution:

    def countCompleteSubarrays1(self, nums: List[int]) -> int:
        # n^2
        ans = 0
        n = len(nums)
        target = len(set(nums))
        for i in range(n):
            ns = set()
            for j in range(i, n):
                ns.add(nums[j])
                if len(ns) == target:
                    ans += 1
        return ans

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        ans = 0
        cnt = Counter()
        left = 0
        for x in nums:
            cnt[x] += 1
            while len(cnt) == m:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().countCompleteSubarrays([5, 5, 5, 5]))
    # 4
    print(Solution().countCompleteSubarrays([1, 3, 1, 2, 2]))
