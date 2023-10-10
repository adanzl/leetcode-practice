"""
 * 给你一个下标从 0 开始的数组 nums 和一个整数 target 。
 * 下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。
 * 请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 3、1 <= target <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/
"""
from typing import List


class Solution:

    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        a, target = divmod(target, sum(nums))
        sm = 0
        LIMIT = 10**10
        ans, n = LIMIT, len(nums)
        if target == 0: return a*n
        l, r = 0, 0
        while l < n:
            while sm < target:
                sm += nums[r % n]
                r += 1
            if sm == target:
                ans = min(ans, r - l)
                if l < r:
                    sm -= nums[l % n]
                    l += 1
            while l < r and sm > target:
                sm -= nums[l % n]
                l += 1
            if sm == target:
                ans = min(ans, r - l)

        return (ans + a*n) if ans != LIMIT else -1


if __name__ == '__main__':
    # 16
    print(Solution().minSizeSubarray([1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6], 56))
    # 2
    print(Solution().minSizeSubarray([1, 2, 3], target=5))
    # 2
    print(Solution().minSizeSubarray([1, 1, 1, 2, 3], target=4))
    # -1
    print(Solution().minSizeSubarray([2, 4, 6, 8], target=3))
