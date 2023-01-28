"""
 * 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中 好 子数组的数目。
 * 一个子数组 arr 如果有 至少 k 对下标 (i, j) 满足 i < j 且 arr[i] == arr[j] ，那么称它是一个 好 子数组。
 * 子数组 是原数组中一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i], k <= 10^9
 * 链接：https://leetcode.cn/problems/count-the-number-of-good-subarrays/
"""
from typing import Counter, List


class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        ans, sm, n = 0, 0, len(nums)
        cnt = Counter()
        l, r = 0, 0
        while r < n:
            while r < n and sm < k:
                sm += cnt[nums[r]]
                cnt[nums[r]] += 1
                r += 1
            if sm < k:
                break
            while l < r and sm >= k:
                ans += n - r + 1
                cnt[nums[l]] -= 1
                sm -= cnt[nums[l]]
                l += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().countGood([3, 1, 4, 3, 2, 2, 4], k=2))
    # 1
    print(Solution().countGood([1, 1, 1, 1, 1], k=10))
