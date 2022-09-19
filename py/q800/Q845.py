"""
 * 把符合下列属性的数组 arr 称为 山脉数组 ：
 * 1、arr.length >= 3
 * 2、存在下标 i（0 < i < arr.length - 1），满足
 * （1）arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 * （2）arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 * 给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。
 * 提示：
 * 1、1 <= arr.length <= 10^4
 * 2、0 <= arr[i] <= 10^4
 * 进阶：
 * 1、你可以仅用一趟扫描解决此问题吗？
 * 2、你可以用 O(1) 空间解决此问题吗？
 * 链接：https://leetcode.cn/problems/longest-mountain-in-array/
"""
from typing import *
from math import *
from collections import *


class Solution:

    def longestMountain(self, arr: List[int]) -> int:
        ans = last_len = 0
        rise = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                rise += 1
                last_len = 0
            elif arr[i] < arr[i - 1]:
                if rise:
                    last_len = rise
                    rise = 0
                if last_len:
                    last_len += 1
                ans = max(ans, last_len)
            else:
                last_len = 0
                rise = 0
        return 0 if ans == 0 else ans + 1


if __name__ == '__main__':
    # 5
    print(Solution().longestMountain([1, 2, 1, 4, 7, 3, 2, 5]))
    # 0
    print(Solution().longestMountain([2, 2, 2]))
    # 3
    print(Solution().longestMountain([2, 3, 2]))
    # 0
    print(Solution().longestMountain([2, 1, 2]))
