"""
 * 给你一个下标从 0 开始的正整数数组 heights ，其中 heights[i] 表示第 i 栋建筑的高度。
 * 如果一个人在建筑 i ，且存在 i < j 的建筑 j 满足 heights[i] < heights[j] ，那么这个人可以移动到建筑 j 。
 * 给你另外一个数组 queries ，其中 queries[i] = [ai, bi] 。第 i 个查询中，Alice 在建筑 ai ，Bob 在建筑 bi 。
 * 请你能返回一个数组 ans ，其中 ans[i] 是第 i 个查询中，Alice 和 Bob 可以相遇的 最左边的建筑 。
 * 如果对于查询 i ，Alice 和 Bob 不能相遇，令 ans[i] 为 -1 。
 * 提示：
 * 1、1 <= heights.length <= 5 * 10^4
 * 2、1 <= heights[i] <= 10^9
 * 3、1 <= queries.length <= 5 * 10^4
 * 4、queries[i] = [ai, bi]
 * 5、0 <= ai, bi <= heights.length - 1
 * 链接：https://leetcode.cn/contest/weekly-contest-372/problems/find-building-where-alice-and-bob-can-meet/
"""
from bisect import bisect_left
from typing import List, Optional

INF = int(10**10)


class SegTree:

    class Node:

        def __init__(self, l: int, r: int, left=None, right=None):
            self.l = l
            self.r = r
            self.dirty = self.mn = self.v = INF  # point
            self.left: Optional[SegTree.Node] = left
            self.right: Optional[SegTree.Node] = right

    # 动态开点线段树模板，取最小值
    def __init__(self, l: int, r: int):
        self.head = SegTree.Node(l, r)

    def addNode(self, l: int, r: int, v):
        self._addNode(self.head, l, r, v)

    def _addNode(self, root: Optional[Node], l, r, v):
        if root is None: return
        mid = (root.l + root.r) >> 1
        if root.left is None:
            root.left = SegTree.Node(root.l, mid)
        if root.right is None:
            root.right = SegTree.Node(mid + 1, root.r)
        if root.l == l and r == root.r:
            root.dirty = v  # point
            root.v = v  # point
            root.mn = v  # point
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
        root.mn = min(root.left.mn, root.right.mn)

    def query(self, l: int, r: int):
        return self._query(self.head, l, r)

    def _query(self, root: Optional[Node], l: int, r: int):
        if root is None:
            return INF  # point
        if root.l == l and root.r == r:
            return root.mn
        self.pushDown(root)
        mid = (root.l + root.r) >> 1
        if r <= mid:
            return self._query(root.left, l, r)
        if l >= mid + 1:
            return self._query(root.right, l, r)
        # point
        return min(self._query(root.left, l, mid), self._query(root.right, mid + 1, r))

    def pushDown(self, root: Node):
        if root.dirty == INF: return
        if root.left is not None: self._addNode(root.left, root.left.l, root.left.r, root.dirty)
        if root.right is not None: self._addNode(root.right, root.right.l, root.right.r, root.dirty)
        root.dirty = INF


class Solution:

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [-1] * n
        LIMIT = 10**5
        st = SegTree(0, LIMIT)
        # 离散化
        st_h = sorted(heights)
        arr = [bisect_left(st_h, num) for num in heights]
        for i in range(len(queries)):
            if queries[i][0] > queries[i][1]:
                queries[i][0], queries[i][1] = queries[i][1], queries[i][0]
        ii = len(heights) - 1
        qq = sorted([[i0, i1, i] for i, (i0, i1) in enumerate(queries)], key=lambda x: (x[1], x[0]), reverse=True)
        for i0, i1, i in qq:
            l = max(arr[i0], arr[i1]) + 1
            while ii >= i1 and ii >= 0:
                st.addNode(arr[ii], arr[ii], ii)
                ii -= 1
            if i0 == i1:
                ans[i] = i0
            elif arr[i0] < arr[i1]:
                ans[i] = i1
            else:
                idx = st.query(l, LIMIT)
                if idx != INF:
                    ans[i] = idx
        return ans


if __name__ == '__main__':
    # [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5]
    print(Solution().leftmostBuildingQueries([1, 2, 1, 2, 1, 2],
                                             [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 0],
                                              [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]))
    # [2,5,-1,5,2]
    print(Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]))
    # [7,6,-1,4,6]
    print(Solution().leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6], queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]))
