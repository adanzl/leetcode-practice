"""
 * 给你一个下标从 0 开始包含 n 个正整数的数组 arr ，和一个正整数 k 。
 * 如果对于每个满足 k <= i <= n-1 的下标 i ，都有 arr[i-k] <= arr[i] ，那么我们称 arr 是 K 递增 的。
 * 1、比方说，arr = [4, 1, 5, 2, 6, 2] 对于 k = 2 是 K 递增的，因为：
 *  arr[0] <= arr[2] (4 <= 5)
 *  arr[1] <= arr[3] (1 <= 2)
 *  arr[2] <= arr[4] (5 <= 6)
 *  arr[3] <= arr[5] (2 <= 2)
 * 2、但是，相同的数组 arr 对于 k = 1 不是 K 递增的（因为 arr[0] > arr[1]），对于 k = 3 也不是 K 递增的（因为 arr[0] > arr[3] ）。
 * 每一次 操作 中，你可以选择一个下标 i 并将 arr[i] 改成任意 正整数。
 * 请你返回对于给定的 k ，使数组变成 K 递增的 最少操作次数 。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、1 <= arr[i], k <= arr.length
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/
"""

from typing import List
from bisect import bisect_right

#
# @lc app=leetcode.cn id=2111 lang=python3
#
# [2111] 使数组 K 递增的最少操作次数
#


# @lc code=start
class Solution:

    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)  #  总长度 减去 最长非下降子序列 LIS 最长上升子序列
        ans = 0
        for i in range(k):  # 起点
            SIZE = 1 + (n - 1 - i) // k
            # f[i] 表示长度为i的最长上升子序列的末尾元素的最小值, 数组的值一定单调不降
            f = []
            for j in range(i, n, k):
                idx = bisect_right(f, arr[j])
                if idx == len(f):
                    f.append(arr[j])
                else:
                    f[idx] = arr[j]
            ans += SIZE - len(f)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().kIncreasing([4, 1, 5, 2, 6, 2], k=2))
    # 2
    print(Solution().kIncreasing([4, 1, 5, 2, 6, 2], k=3))
    # 4
    print(Solution().kIncreasing([5, 4, 3, 2, 1], k=1))
