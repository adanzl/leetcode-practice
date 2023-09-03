"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 x 。
 * 请你找到数组中下标距离至少为 x 的两个元素的 差值绝对值 的 最小值 。
 * 换言之，请你找到两个下标 i 和 j ，满足 abs(i - j) >= x 且 abs(nums[i] - nums[j]) 的值最小。
 * 请你返回一个整数，表示下标距离至少为 x 的两个元素之间的差值绝对值的 最小值 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、0 <= x < nums.length
 * 链接：https://leetcode.cn/problems/minimum-absolute-difference-between-elements-with-constraint/
"""
import bisect
from typing import List


class Solution:

    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        MX = 10**10 + 7
        ans = MX
        arr = []
        for i, num in enumerate(nums):
            idx = bisect.bisect_left(arr, num)
            l = arr[idx - 1] if idx else MX
            r = arr[idx] if idx < len(arr) else MX
            ans = min(ans, min(abs(num - l), abs(num - r)))
            if i >= x - 1:
                bisect.insort(arr, nums[i - x + 1])
        return ans


if __name__ == '__main__':
    # 999999999
    print(Solution().minAbsoluteDifference([1, 1000000000], 1))
    # 0
    print(Solution().minAbsoluteDifference([4, 3, 2, 4], x=2))
    # 1
    print(Solution().minAbsoluteDifference([5, 3, 2, 10, 15], x=1))
    # 3
    print(Solution().minAbsoluteDifference([1, 2, 3, 4], x=3))
