"""
 * 给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：
 * 1、令 x 为你数组里所有元素的和
 * 2、选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
 * 3、你可以重复该过程任意次
 * 如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。
 * 提示：
 * 1、N == target.length
 * 2、1 <= target.length <= 5 * 10^4
 * 3、1 <= target[i] <= 10^9
 * 链接：https://leetcode.cn/problems/construct-target-array-with-multiple-sums/
"""

from heapq import heapify, heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=1354 lang=python3
#
# [1354] 多次求和构造目标数组
#


# @lc code=start
class Solution:

    def isPossible(self, target: List[int]) -> bool:
        n, sm = len(target), sum(target)
        h = [-num for num in target if num != 1]
        heapify(h)
        while h:
            num = -heappop(h)
            sm -= num
            if sm == 0: return False
            if sm == 1: return True
            if num <= sm:
                return False
            r = num % sm
            sm += r
            if r != 1:
                heappush(h, -r)
        return True


# @lc code=end

if __name__ == '__main__':
    # False
    print(Solution().isPossible([2, 900000002]))
    # False
    print(Solution().isPossible([1, 1, 1, 2]))
    # True
    print(Solution().isPossible([1, 1_000_000_000]))
    # True
    print(Solution().isPossible([9, 3, 5]))
    # True
    print(Solution().isPossible([8, 5]))
