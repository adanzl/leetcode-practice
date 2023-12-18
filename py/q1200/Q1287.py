"""
 * 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
 * 请你找到并返回这个整数
 * 提示：
 * 1、1 <= arr.length <= 10^4
 * 2、0 <= arr[i] <= 10^5
 * 链接：https://leetcode.cn/problems/element-appearing-more-than-25-in-sorted-array
"""
import bisect
from typing import List


#
# @lc app=leetcode.cn id=1287 lang=python3
#
#
class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))
