"""
 * 有 n 个人前来排队买票，其中第 0 人站在队伍 最前方 ，第 (n - 1) 人站在队伍 最后方 。
 * 给你一个下标从 0 开始的整数数组 tickets ，数组长度为 n ，其中第 i 人想要购买的票数为 tickets[i] 。
 * 每个人买票都需要用掉 恰好 1 秒 。一个人 一次只能买一张票 ，如果需要购买更多票，他必须走到  队尾 重新排队（瞬间 发生，不计时间）。如果一个人没有剩下需要买的票，那他将会 离开 队伍。
 * 返回位于位置 k（下标从 0 开始）的人完成买票需要的时间（以秒为单位）。
 * 提示：
 * n == tickets.length
 * 1 <= n <= 100
 * 1 <= tickets[i] <= 100
 * 0 <= k < n
 * 链接：https://leetcode.cn/problems/time-needed-to-buy-tickets
"""

from bisect import bisect_left
from typing import List

#
# @lc app=leetcode.cn id=2073 lang=python3
#
# [2073] 买票需要的时间
#


# @lc code=start
class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        d = dict([(i, tickets[i]) for i in range(len(tickets))])
        while k in d:
            if d[k] == 1:
                ans += bisect_left(sorted(d.keys()), k) + 1
                break
            else:
                ans += len(d)
            for key, val in list(d.items()):
                if val > 1:
                    d[key] = val - 1
                else:
                    d.pop(key)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 154
    print(Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8], 3))
    # 6
    print(Solution().timeRequiredToBuy([2, 3, 2], k=2))
    # 8
    print(Solution().timeRequiredToBuy([5, 1, 1, 1], k=0))
