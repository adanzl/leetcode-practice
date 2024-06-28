"""
 * 一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，
 * 其中 rooms[i] = [roomId_i, size_i] 表示有一个房间号为 roomIdi 的房间且它的面积为 size_i 。
 * 每一个房间号 roomIdi 保证是 独一无二 的。
 * 同时给你 k 个查询，用二维数组 queries 表示，其中 queries[j] = [preferred_j, minSize_j] 。
 * 第 j 个查询的答案是满足如下条件的房间 id ：
 * 1、房间的面积 至少 为 minSize_j ，且
 * 2、abs(id - preferred_j) 的值 最小 ，其中 abs(x) 是 x 的绝对值。
 * 如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。
 * 请你返回长度为 k 的数组 answer ，其中 answer[j] 为第 j 个查询的结果。
 * 提示：
 * 1、n == rooms.length
 * 2、1 <= n <= 10^5
 * 3、k == queries.length
 * 4、1 <= k <= 10^4
 * 5、1 <= roomId_i, preferred_j <= 10^7
 * 6、1 <= size_i, minSize_j <= 10^7
 * 链接：https://leetcode.cn/problems/closest-room/
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=1847 lang=python3
#
# [1847] 最近的房间
#


# @lc code=start
class Solution:

    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort()
        k = len(queries)
        ans = [-1] * k
        qq = sorted([[q[0], q[1], i] for i, q in enumerate(queries)], key=lambda x: (x[1], x[0]))
        for p, m, i in qq:
            idx = bisect.bisect_right(rooms, [p, 0])
            vv, v_id = 0x3c3c3c3c3c3c, -1
            while idx > 0 and rooms[idx - 1][1] < m:
                rooms.pop(idx - 1)
                idx -= 1
            if idx > 0:
                if abs(p - rooms[idx - 1][0]) < vv:
                    vv, v_id = abs(p - rooms[idx - 1][0]), rooms[idx - 1][0]
            while idx < len(rooms) and rooms[idx][1] < m:
                rooms.pop(idx)
            if idx < len(rooms):
                if abs(p - rooms[idx][0]) < vv:
                    vv, v_id = min(vv, abs(p - rooms[idx][0])), rooms[idx][0]
            ans[i] = v_id
        return ans


# @lc code=end

if __name__ == '__main__':
    # [14,15,9,1,17,10,14,10,17,9]
    print(Solution().closestRoom(
        [[15, 19], [11, 10], [12, 1], [17, 6], [1, 6], [10, 21], [13, 7], [14, 25], [19, 3], [9, 11]],
        [[14, 14], [20, 17], [6, 8], [1, 6], [21, 4], [4, 16], [3, 22], [2, 21], [24, 6], [6, 1]]))
    # [3,-1,3]
    print(Solution().closestRoom([[2, 2], [1, 2], [3, 2]], queries=[[3, 1], [3, 3], [5, 2]]))
    # [2,1,3]
    print(Solution().closestRoom([[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], queries=[[2, 3], [2, 4], [2, 5]]))
