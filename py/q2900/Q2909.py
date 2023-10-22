"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 如果下标三元组 (i, j, k) 满足下述全部条件，则认为它是一个 山形三元组 ：
 * 1、i < j < k
 * 2、nums[i] < nums[j] 且 nums[k] < nums[j]
 * 请你找出 nums 中 元素和最小 的山形三元组，并返回其 元素和 。如果不存在满足条件的三元组，返回 -1 。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^8
 * 链接：https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/
"""
import bisect
from typing import List


class Solution:

    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_r = []
        LIMIT = 10**10
        ans = LIMIT
        arr = []
        for i in range(n - 1, -1, -1):
            if arr and arr[0] < nums[i]:
                min_r.append(arr[0])
            else:
                min_r.append(-1)
            bisect.insort(arr, nums[i])
        arr = []
        for i in range(n):
            if arr and arr[0] < nums[i] and min_r[n - 1 - i] != -1:
                ans = min(ans, nums[i] + arr[0] + min_r[n - 1 - i])
            bisect.insort(arr, nums[i])
        return ans if ans != LIMIT else -1


if __name__ == '__main__':
    # 9
    print(Solution().minimumSum([8, 6, 1, 5, 3]))
    # 13
    print(Solution().minimumSum([5, 4, 8, 7, 10, 2]))
    # -1
    print(Solution().minimumSum([6, 5, 4, 3, 4, 5]))
