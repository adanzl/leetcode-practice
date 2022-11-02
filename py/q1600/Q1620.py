"""
 * 给你一个数组 towers 和一个整数 radius 。
 * 数组  towers  中包含一些网络信号塔，其中 towers[i] = [xi, yi, qi] 表示第 i 个网络信号塔的坐标是 (xi, yi) 且信号强度参数为 qi 。所有坐标都是在  X-Y 坐标系内的 整数 坐标。两个坐标之间的距离用 欧几里得距离 计算。
 * 整数 radius 表示一个塔 能到达 的 最远距离 。如果一个坐标跟塔的距离在 radius 以内，那么该塔的信号可以到达该坐标。在这个范围以外信号会很微弱，所以 radius 以外的距离该塔是 不能到达的 。
 * 如果第 i 个塔能到达 (x, y) ，那么该塔在此处的信号为 ⌊qi / (1 + d)⌋ ，其中 d 是塔跟此坐标的距离。一个坐标的 信号强度 是所有 能到达 该坐标的塔的信号强度之和。
 * 请你返回数组 [cx, cy] ，表示 信号强度 最大的 整数 坐标点 (cx, cy) 。如果有多个坐标网络信号一样大，请你返回字典序最小的 非负 坐标。
 * 注意：
 * 1、坐标 (x1, y1) 字典序比另一个坐标 (x2, y2) 小，需满足以下条件之一：
 * 2、要么 x1 < x2 ，
 * 3、要么 x1 == x2 且 y1 < y2 。
 * 4、⌊val⌋ 表示小于等于 val 的最大整数（向下取整函数）。
 * 提示：
 * 1、1 <= towers.length <= 50
 * 2、towers[i].length == 3
 * 3、0 <= xi, yi, qi <= 50
 * 4、1 <= radius <= 50
 * 链接：https://leetcode.cn/problems/coordinate-with-maximum-network-quality/
"""
from typing import List


class Solution:

    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        cx = cy = max_quality = 0
        for x in range(x_max + 1):
            for y in range(y_max + 1):
                quality = 0
                for tx, ty, q in towers:
                    d = (x - tx)**2 + (y - ty)**2
                    if d <= radius**2:
                        quality += int(q / (1 + d**0.5))
                if quality > max_quality:
                    cx, cy, max_quality = x, y, quality
        return [cx, cy]


if __name__ == '__main__':
    # [2,1]
    print(Solution().bestCoordinate([[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius=2))
    # [23,11]
    print(Solution().bestCoordinate(towers=[[23, 11, 21]], radius=9))
    # [1,2]
    print(Solution().bestCoordinate([[1, 2, 13], [2, 1, 7], [0, 1, 9]], radius=2))
