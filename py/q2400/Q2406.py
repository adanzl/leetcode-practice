from heapq import *
from typing import *
'''
给你一个二维整数数组 intervals ，其中 intervals[i] = [left_i, right_i] 表示 闭 区间 [left_i, right_i] 。
你需要将 intervals 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。
请你返回 最少 需要划分成多少个组。
如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 [1, 5] 和 [5, 8] 相交。
提示：
1、1 <= intervals.length <= 10^5
2、intervals[i].length == 2
3、1 <= left_i <= right_i <= 10^6
链接：https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups
'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        h = []
        for l, r in intervals:
            if h and h[0] < l:
                heapreplace(h, r)
            else:
                heappush(h, r)
        return len(h)


if __name__ == '__main__':
    # 3
    print(Solution().minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
    # 1
    print(Solution().minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]))
