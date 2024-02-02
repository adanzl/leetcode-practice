"""
 * 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。
 * 请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。
 * 提示：10 <= low <= high <= 10^9
 * 链接：https://leetcode.cn/problems/sequential-digits
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=1291 lang=python3
#
# [1291] 顺次数
#
# @lc code=start
arr = []
ss = '123456789'
for i in range(2, 10):
    arr.append([])
    for a in range(10 - i):
        arr[-1].append(int(ss[a:a + i]))
arr.append([])


class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        l_low, l_high = len(str(low)), len(str(high))
        i_low_l = bisect.bisect_left(arr[l_low - 2], low)
        i_low_r = len(arr[l_low - 2])
        if l_low == l_high:
            i_low_r = bisect.bisect_right(arr[l_low - 2], high)
        ans.extend(arr[l_low - 2][i_low_l:i_low_r])
        for i in range(l_low + 1, l_high):
            ans.extend(arr[i - 2])
        if l_low != l_high:
            i_high_r = bisect.bisect_right(arr[l_high - 2], high)
            ans.extend(arr[l_high - 2][:i_high_r])
        return ans


# @lc code=end

if __name__ == '__main__':
    # [123,234]
    print(Solution().sequentialDigits(100, high=300))
    # [1234,2345,3456,4567,5678,6789,12345]
    print(Solution().sequentialDigits(1000, high=13000))
    # [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
    print(Solution().sequentialDigits(10, 1000000000))
