"""
 * 有 n 个朋友在举办一个派对，这些朋友从 0 到 n - 1 编号。
 * 派对里有 无数 张椅子，编号为 0 到 infinity 。
 * 当一个朋友到达派对时，他会占据 编号最小 且未被占据的椅子。
 * 比方说，当一个朋友到达时，如果椅子 0 ，1 和 5 被占据了，那么他会占据 2 号椅子。
 * 当一个朋友离开派对时，他的椅子会立刻变成未占据状态。
 * 如果同一时刻有另一个朋友到达，可以立即占据这张椅子。
 * 给你一个下标从 0 开始的二维整数数组 times ，其中 times[i] = [arrival_i, leaving_i] 表示第 i 个朋友到达和离开的时刻，
 * 同时给你一个整数 targetFriend 。所有到达时间 互不相同 。
 * 请你返回编号为 targetFriend 的朋友占据的 椅子编号 。
 * 提示：
 * 1、n == times.length
 * 2、2 <= n <= 10^4
 * 3、times[i].length == 2
 * 4、1 <= arrival_i < leaving_i <= 10^5
 * 5、0 <= targetFriend <= n - 1
 * 6、每个 arrival_i 时刻 互不相同 。
 * 链接：https://leetcode.cn/problems/the-number-of-the-smallest-unoccupied-chair
"""

from heapq import heappop, heappush
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1942 lang=python3
# @lcpr version=20001
#
# [1942] 最小未被占据椅子的编号
#


# @lc code=start
class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        h_ticket = []
        f = 0
        record = []
        for i, (a, l) in enumerate(times):
            record.append([a, 1, i])
            record.append([l, 0, i])
        t_map = {}
        for _, s, i in sorted(record):
            if s == 1:  # arrival_i
                if h_ticket:
                    ff = heappop(h_ticket)
                else:
                    ff = f
                    f += 1
                if i == targetFriend:
                    return ff
                t_map[i] = ff
            else:  # leave_i
                heappush(h_ticket, t_map[i])
        return 0


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().smallestChair(
        [[18, 19], [10, 11], [21, 22], [5, 6], [2, 3], [6, 7], [43, 44], [48, 49], [53, 54], [12, 13], [20, 21],
         [34, 35], [17, 18], [1, 2], [35, 36], [16, 17], [9, 10], [14, 15], [25, 26], [37, 38], [30, 31], [50, 51],
         [22, 23], [3, 4], [27, 28], [29, 30], [33, 34], [39, 40], [49, 50], [15, 16], [4, 5], [46, 47], [51, 52],
         [32, 33], [11, 12], [28, 29], [47, 48], [36, 37], [40, 41], [42, 43], [52, 53], [41, 42], [31, 32], [23, 24],
         [8, 9], [19, 20], [24, 25], [26, 27], [45, 46], [44, 45], [7, 8], [13, 14], [38, 39]], 8))
    # 1
    print(Solution().smallestChair([[1, 4], [2, 3], [4, 6]], targetFriend=1))
    # 2
    print(Solution().smallestChair([[3, 10], [1, 5], [2, 6]], targetFriend=0))
