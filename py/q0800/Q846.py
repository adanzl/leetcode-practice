"""
 * Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，
 * 并且由 groupSize 张连续的牌组成。
 * 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌上的数值。
 * 如果她可能重新排列这些牌，返回 true ；否则，返回 false 。
 * 注意：此题目与 1296 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
 * 提示：
 * 1、1 <= hand.length <= 10^4
 * 2、0 <= hand[i] <= 10^9
 * 3、1 <= groupSize <= hand.length
 * 链接：https://leetcode.cn/problems/hand-of-straights
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=1296 lang=python3
#
# [1296] 划分数组为连续数字的集合
#


# @lc code=start
class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: return True
        h = []  # end-size
        for num in sorted(hand):
            if h and num - h[0][0] == 1:
                end, size = heappop(h)
                if size < groupSize - 1:
                    heappush(h, [end + 1, size + 1])
            else:
                heappush(h, [num, 1])
        return len(h) == 0


# @lc code=end

if __name__ == '__main__':
    # True
    print(Solution().isNStraightHand([1, 2, 3], 1))
    # True
    print(Solution().isNStraightHand([1, 2, 3, 3, 4, 4, 5, 6], 4))
    # True
    print(Solution().isNStraightHand([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
    # True
    print(Solution().isNStraightHand([3, 3, 2, 2, 1, 1], 3))
    # False
    print(Solution().isNStraightHand([1, 2, 3, 4], 3))
