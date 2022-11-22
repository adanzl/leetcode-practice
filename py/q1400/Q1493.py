"""
 * 给你一个二进制数组 nums ，你需要从中删掉一个元素。
 * 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
 * 如果不存在这样的子数组，请返回 0 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、nums[i] 要么是 0 要么是 1 。
 * 链接：https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/
"""
from typing import List


class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        arr = nums[:]
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        for i in range(1, n):
            if nums[i] == nums[i - 1] == 1:
                r1, r2 = find(i), find(i - 1)
                parent[r2] = parent[r1]
                arr[r1] += arr[r2]
        ans = 0
        for i in range(n):
            ret = 0
            if nums[i]:
                ret = arr[parent[find(i)]] - 1
            else:
                ret = (arr[parent[find(i - 1)]] if i else 0) + (arr[parent[find(i + 1)]] if i < n - 1 else 0)
            ans = max(ans, ret)
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().longestSubarray([1, 1, 0, 1]))
    # 5
    print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    # 2
    print(Solution().longestSubarray([1, 1, 1]))
    #
    # print(Solution().longestSubarray())