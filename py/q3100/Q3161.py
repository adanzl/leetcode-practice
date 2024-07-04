"""
 * 有一条无限长的数轴，原点在 0 处，沿着 x 轴 正 方向无限延伸。
 * 给你一个二维数组 queries ，它包含两种操作：
 * 1、操作类型 1 ：queries[i] = [1, x] 。在距离原点 x 处建一个障碍物。数据保证当操作执行的时候，位置 x 处 没有 任何障碍物。
 * 2、操作类型 2 ：queries[i] = [2, x, sz] 。
 *      判断在数轴范围 [0, x] 内是否可以放置一个长度为 sz 的物块，这个物块需要 完全 放置在范围 [0, x] 内。
 *      如果物块与任何障碍物有重合，那么这个物块 不能 被放置，但物块可以与障碍物刚好接触。注意，你只是进行查询，并 不是 真的放置这个物块。
 *      每个查询都是相互独立的。
 * 请你返回一个 boolean 数组results ，如果第 i 个操作类型 2 的操作你可以放置物块，那么 results[i] 为 true ，否则为 false 。
 * 提示：
 * 1、1 <= queries.length <= 15 * 10^4
 * 2、2 <= queries[i].length <= 3
 * 3、1 <= queries[i][0] <= 2
 * 4、1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
 * 5、输入保证操作 1 中，x 处不会有障碍物。
 * 6、输入保证至少有一个操作类型 2 。
 * 链接：https://leetcode.cn/problems/block-placement-queries/description/
"""
import bisect
from typing import List, Optional

INF = int(10**10)


class Node:

    def __init__(self, l: int, r: int, left=None, right=None):
        self.l = l
        self.r = r
        self.dirty = self.max = self.v = -INF
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


class SegTree:
    # 动态开点线段树模板，取最大值
    def __init__(self, l: int, r: int):
        self.head = Node(l, r)

    def addNode(self, l: int, r: int, v):
        self._addNode(self.head, l, r, v)

    def _addNode(self, root: Optional[Node], l, r, v):
        if root is None: return
        mid = (root.l + root.r) >> 1
        if root.left is None:
            root.left = Node(root.l, mid)
        if root.right is None:
            root.right = Node(mid + 1, root.r)
        if root.l == l and r == root.r:
            root.dirty = v  # point
            root.v = v  # point
            root.max = v  # point
            return

        self.pushDown(root)
        if r <= mid:
            self._addNode(root.left, l, r, v)
        elif l >= mid + 1:
            self._addNode(root.right, l, r, v)
        else:
            self._addNode(root.left, l, mid, v)
            self._addNode(root.right, mid + 1, r, v)

        # point
        root.max = max(root.left.max, root.right.max)

    def query(self, l: int, r: int):
        return self._query(self.head, l, r)

    def _query(self, root: Optional[Node], l: int, r: int):
        if root is None:
            return 0
        if root.l == l and root.r == r:
            return root.max
        self.pushDown(root)
        mid = (root.l + root.r) >> 1
        if r <= mid:
            return self._query(root.left, l, r)
        if l >= mid + 1:
            return self._query(root.right, l, r)
        # point
        return max(self._query(root.left, l, mid), self._query(root.right, mid + 1, r))

    def pushDown(self, root: Node):
        if root.dirty == -INF: return
        if root.left is not None: self._addNode(root.left, root.left.l, root.left.r, root.dirty)
        if root.right is not None: self._addNode(root.right, root.right.l, root.right.r, root.dirty)
        root.dirty = -INF


class Solution:

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        INF = 0x3c3c3c3c3c
        pos = [0]
        ans = []
        t = SegTree(0, 10**6)
        t.addNode(0, 0, INF)
        for q in queries:
            if q[0] == 1:
                ii = bisect.bisect(pos, q[1])
                i0 = ii - 1
                t.addNode(pos[i0], pos[i0], q[1] - pos[i0])
                if ii < len(pos):
                    t.addNode(q[1], q[1], pos[ii] - q[1])
                else:
                    t.addNode(q[1], q[1], INF)
                bisect.insort(pos, q[1])
            else:
                ii = bisect.bisect_right(pos, q[1])
                mx = q[1] - pos[ii - 1]
                if ii > 1:
                    mx = max(t.query(0, pos[ii - 1] - 1), mx)
                ans.append(q[2] <= mx)
        return ans


if __name__ == '__main__':
    # [False]
    print(Solution().getResults([[1, 1], [1, 11], [1, 4], [1, 8], [2, 13, 7]]))
    # [True]
    print(Solution().getResults([[2, 1, 1]]))
    # [false,true,true]
    print(Solution().getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]))
    # [true,true,false]
    print(Solution().getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]))
