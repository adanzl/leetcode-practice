"""
 * 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
 * 如果可以，请返回 true；否则，返回 false。
 * 注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/
 * 提示：
 * 1、1 <= k <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 划分数组为连续数字的集合
#


# @lc code=start
class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        h = []  # end-size
        for num in sorted(nums):
            if h and num - h[0][0] == 1:
                end, size = heappop(h)
                if size < k - 1:
                    heappush(h, [end + 1, size + 1])
            else:
                heappush(h, [num, 1])
        return len(h) == 0


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isPossibleDivide([1, 2, 3], k=1))
    # True
    print(Solution().isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], k=4))
    # True
    print(Solution().isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))
    # True
    print(Solution().isPossibleDivide([3, 3, 2, 2, 1, 1], k=3))
    # False
    print(Solution().isPossibleDivide([1, 2, 3, 4], k=3))
