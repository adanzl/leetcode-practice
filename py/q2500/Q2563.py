"""
 * 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。
 * 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：
 * 1、0 <= i < j < n，且
 * 2、lower <= nums[i] + nums[j] <= upper
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums.length == n
 * 3、-10^9 <= nums[i] <= 10^9
 * 4、-10^9 <= lower <= upper <= 10^9
 * 链接：https://leetcode.cn/problems/count-the-number-of-fair-pairs/
"""
from bisect import bisect_left, insort
from typing import List


class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        arr = []
        ans = 0
        for num in nums:
            u, l = bisect_left(arr, upper - num + 1), bisect_left(arr, lower - num)
            ans += u - l
            insort(arr, num)
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().countFairPairs([0, 1, 7, 4, 4, 5], lower=3, upper=6))
    # 1
    print(Solution().countFairPairs([1, 7, 9, 2, 5], lower=11, upper=11))
