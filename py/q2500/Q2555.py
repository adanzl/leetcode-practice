"""
 * 在 X轴 上有一些奖品。给你一个整数数组 prizePositions ，它按照 非递减 顺序排列，其中 prizePositions[i] 是第 i 件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 k 。
 * 你可以选择两个端点为整数的线段。每个线段的长度都必须是 k 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。
 * 比方说 k = 2 ，你可以选择线段 [1, 3] 和 [2, 4] ，你可以获得满足 1 <= prizePositions[i] <= 3 或者 2 <= prizePositions[i] <= 4 的所有奖品 i 。
 * 请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。
 * 提示：
 * 1、1 <= prizePositions.length <= 10^5
 * 2、1 <= prizePositions[i] <= 10^9
 * 3、0 <= k <= 10^9
 * 4、prizePositions 有序非递减。
 * 链接：https://leetcode.cn/problems/maximize-win-from-two-segments/
"""
from bisect import bisect_left
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
    
    def maximizeWin(self, pp: List[int], k: int) -> int:
        pre_sum = [0] * (len(pp) + 1)
        l, ans = 0, 0
        for r, p in enumerate(pp):
            while p - pp[l] > k:
                l += 1
            ans = max(ans, r - l + 1 + pre_sum[l])
            pre_sum[r + 1] = max(pre_sum[r], r - l + 1)
        return ans

    def maximizeWin1(self, prizePositions: List[int], k: int) -> int:
        pre_sum = [0, 1]
        keys = [prizePositions[0]]
        for i in range(1, len(prizePositions)):
            if prizePositions[i] == prizePositions[i - 1]:
                pre_sum[-1] += 1
            else:
                pre_sum.append(pre_sum[-1] + 1)
                keys.append(prizePositions[i])
        LIMIT = len(keys)
        st = SegTree(0, LIMIT)
        for i, num in enumerate(keys):
            idx = min(len(keys) - 1, bisect_left(keys, num + k))
            if num + k < keys[idx]:
                idx -= 1
            st.addNode(i, i, pre_sum[idx + 1] - pre_sum[i])
        ans = 0
        for i, num in enumerate(keys):
            idx = min(len(keys) - 1, bisect_left(keys, num + k))
            if num + k < keys[idx]:
                idx -= 1
            ans = max(ans, pre_sum[idx + 1] - pre_sum[i] + max(0, st.query(idx + 1, LIMIT)))
        return ans


if __name__ == '__main__':
    # 7
    print(Solution().maximizeWin([1, 1, 2, 2, 3, 3, 5], k=2))
    # 4
    print(Solution().maximizeWin([1, 1, 3, 6, 6], k=0))
    # 2
    print(Solution().maximizeWin([1, 2, 3, 4], k=0))
