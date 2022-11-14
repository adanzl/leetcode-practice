"""
 * n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
 * 如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
 * 给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
 * 提示：
 * 1、1 <= stones.length <= 1000
 * 2、0 <= xi, yi <= 10^4
 * 3、不会有两块石头放在同一个坐标点上
 * 链接：https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/
"""
from collections import defaultdict
from typing import List


class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:
        # 此处求最大的移除个数，本质上是求联通组的个数，总节点数-联通组个数
        size = 1000
        n = len(stones)
        x_dic, y_dic = defaultdict(list), defaultdict(list)
        parent = {}

        def find(x):
            if x not in parent or parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        ans = n
        for x1, y1 in stones:
            for x2, y2 in x_dic[x1]:
                r1, r2 = find(x1 * size + y1), find(x2 * size + y2)
                if r1 != r2:
                    ans -= 1
                    parent[r2] = r1
            for x2, y2 in y_dic[y1]:
                r1, r2 = find(x1 * size + y1), find(x2 * size + y2)
                if r1 != r2:
                    ans -= 1
                    parent[r2] = r1
            x_dic[x1].append([x1, y1])
            y_dic[y1].append([x1, y1])
        return n - ans


if __name__ == '__main__':
    # 3
    print(Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
    # 5
    print(Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
    # 0
    print(Solution().removeStones([[0, 0]]))
