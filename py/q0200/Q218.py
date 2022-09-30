"""
 * 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。
 * 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [left_i, right_i, height_i] 表示：
 * 1、left_i 是第 i 座建筑物左边缘的 x 坐标。
 * 2、right_i 是第 i 座建筑物右边缘的 x 坐标。
 * 3、height_i 是第 i 座建筑物的高度。
 * 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
 * 关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
 * 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
 * 三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
 * 提示：
 * 1、1 <= buildings.length <= 10^4
 * 2、0 <= left_i < right_i <= 2^31 - 1
 * 3、1 <= height_i <= 2^31 - 1
 * 4、buildings 按 left_i 非递减排序
 * 链接：https://leetcode-cn.com/problems/the-skyline-problem
"""
from typing import *
from heapq import *


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        all_lines = []  # x-height
        for b in buildings:
            all_lines.append([b[0], b[2]])
            all_lines.append([b[1], -b[2]])
        all_lines.sort(key=lambda x: (x[0], -x[1]))
        h = [0]
        c = Counter(h)
        for line in all_lines:
            height = abs(line[1])
            if line[1] > 0:  # up
                if height > -h[0]:
                    ans.append([line[0], height])
                heappush(h, -height)
                c[height] += 1
            else:  # down
                c[height] -= 1
                while c[-h[0]] == 0:
                    heappop(h)
                if height > -h[0]:
                    ans.append([line[0], -h[0]])
        return ans


if __name__ == '__main__':
    # [[0,3], [1,0]]
    print(Solution().getSkyline([[0, 1, 3]]))
    # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # [[0,3],[5,0]]
    print(Solution().getSkyline([[0, 2, 3], [2, 5, 3]]))
