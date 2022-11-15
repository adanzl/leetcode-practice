"""
 * 给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
 * 全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
 * 1、0 <= i < j < n
 * 2、nums[i] > nums[j]
 * 局部倒置 的数目等于满足下述条件的下标 i 的数目：
 * 1、0 <= i < n - 1
 * 2、nums[i] > nums[i + 1]
 * 当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
 * 提示：
 * 1、n == nums.length
 * 2、1 <= n <= 5000
 * 3、0 <= nums[i] < n
 * 4、nums 中的所有整数 互不相同
 * 5、nums 是范围 [0, n - 1] 内所有数字组成的一个排列
 * 链接：https://leetcode.cn/problems/global-and-local-inversions/
"""
from bisect import bisect_right, insort
from typing import List


class Solution:

    def isIdealPermutation(self, nums: List[int]) -> bool:
        a, b = 0, 0
        arr = []
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i - 1]: b += 1
            a += len(arr) - bisect_right(arr, nums[i])
            insort(arr, nums[i])
        return a == b


if __name__ == '__main__':
    # True
    print(Solution().isIdealPermutation([1, 0, 2]))
    # False
    print(Solution().isIdealPermutation([1, 2, 0]))