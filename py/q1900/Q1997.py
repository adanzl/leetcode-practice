"""
 * 你需要访问 n 个房间，房间从 0 到 n - 1 编号。同时，每一天都有一个日期编号，从 0 开始，依天数递增。你每天都会访问一个房间。
 * 最开始的第 0 天，你访问 0 号房间。给你一个长度为 n 且 下标从 0 开始 的数组 nextVisit 。
 * 在接下来的几天中，你访问房间的 次序 将根据下面的 规则 决定：
 * 1、假设某一天，你访问 i 号房间。
 * 2、如果算上本次访问，访问 i 号房间的次数为 奇数 ，那么 第二天 需要访问 nextVisit[i] 所指定的房间，其中 0 <= nextVisit[i] <= i 。
 * 3、如果算上本次访问，访问 i 号房间的次数为 偶数 ，那么 第二天 需要访问 (i + 1) mod n 号房间。
 * 请返回你访问完所有房间的第一天的日期编号。题目数据保证总是存在这样的一天。
 * 由于答案可能很大，返回对 10^9 + 7 取余后的结果。
 * 提示：
 * 1、n == nextVisit.length
 * 2、2 <= n <= 10^5
 * 3、0 <= nextVisit[i] <= i
 * 链接：https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=1997 lang=python3
#
# [1997] 访问完所有房间的第一天
#


# @lc code=start
class Solution:

    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        f = [0] * n
        for i in range(n - 1):
            f[i + 1] = (f[i] + f[i] - f[nextVisit[i]] + 2) % (10**9 + 7)
        return f[-1]


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().firstDayBeenInAllRooms([0, 0, 2]))
    # 2
    print(Solution().firstDayBeenInAllRooms([0, 0]))
    # 6
    print(Solution().firstDayBeenInAllRooms([0, 1, 2, 0]))
