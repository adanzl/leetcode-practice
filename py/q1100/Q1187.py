"""
 * 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
 * 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，
 * 然后进行赋值运算 arr1[i] = arr2[j]。
 * 如果无法让 arr1 严格递增，请返回 -1。
 * 提示：
 * 1、1 <= arr1.length, arr2.length <= 2000
 * 2、0 <= arr1[i], arr2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/make-array-strictly-increasing/
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        idx = 1
        while idx < len(arr2):
            if arr2[idx] == arr2[idx - 1]:
                del arr2[idx]
            else:
                idx += 1
        n, m = len(arr1), len(arr2)
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):  # j<i
            idx_i = bisect_left(arr2, arr1[i])
            for j in range(i - 1, -1, -1):
                if dp[j] >= 0:
                    # end with arr1[i]
                    if arr1[i] > arr1[j] and idx_i - bisect_right(arr2, arr1[j]) >= i - j - 1:
                        if dp[i] == -1 or dp[j] + i - j - 1 < dp[i]:
                            dp[i] = dp[j] + i - j - 1
            # change all
            if idx_i >= i:
                if dp[i] == -1 or i < dp[i]:
                    dp[i] = i
        for i in range(1, min(n, m)):
            if dp[n - i - 1] >= 0 and arr1[n - 1 - i] < arr2[m - i]:
                if dp[-1] == -1 or dp[-1] > dp[n - i - 1] + i:
                    dp[-1] = dp[n - i - 1] + i
        if m >= n:
            if dp[-1] == -1 or dp[-1] > n:
                dp[-1] = n
        return dp[-1]


if __name__ == '__main__':
    # 8
    print(Solution().makeArrayIncreasing([5, 16, 19, 2, 1, 12, 7, 14, 5, 16], [6, 17, 4, 3, 6, 13, 4, 3, 18, 17, 16, 7, 14, 1, 16]))
    # 5
    print(Solution().makeArrayIncreasing([0, 11, 6, 1, 4, 3], [5, 4, 11, 10, 1, 0]))
    # 2
    print(Solution().makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1]))
    # 1
    print(Solution().makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]))
    # -1
    print(Solution().makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]))
