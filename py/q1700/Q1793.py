"""
 * 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
 * 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
 * 请你返回 好 子数组的最大可能 分数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 2 * 10^4
 * 3、0 <= k < nums.length
 * 链接：https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
"""
from typing import List


class Solution:

    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        n = len(nums)
        ans, mn = 0, nums[k]
        while l >= 0 or r <= n - 1:
            while l >= 0 and nums[l] >= mn:
                l -= 1
            while r <= n - 1 and nums[r] >= mn:
                r += 1
            ans = max(ans, (r - l - 1) * mn)
            vl, vr = 0 if l < 0 else nums[l], 0 if r > n - 1 else nums[r]
            if vl < vr:
                mn = min(mn, nums[r])
                r += 1
            else:
                mn = min(mn, nums[l])
                l -= 1
        return ans


if __name__ == '__main__':
    # 9732
    print(Solution().maximumScore([6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], 5))
    # 15
    print(Solution().maximumScore([1, 4, 3, 7, 4, 5], 3))
    # 20
    print(Solution().maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0))
