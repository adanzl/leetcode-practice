"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两个数组的大小都为 n ，同时给你一个整数 diff ，统计满足以下条件的 数对 (i, j) ：
 * 1、0 <= i < j <= n - 1 且
 * 2、nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
 * 请你返回满足条件的 数对数目 。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、2 <= n <= 10^5
 * 3、-10^4 <= nums1[i], nums2[i] <= 10^4
 * 4、-10^4 <= diff <= 10^4
 * 链接：https://leetcode.cn/problems/number-of-pairs-satisfying-inequality/
"""
from typing import Optional, List
from bisect import insort, bisect_right


class Node:

    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.dirty = self.sum = self.v = 0  # point
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class SegTree:
    # 动态开点线段树模板，累加，取和
    def __init__(self, l: int, r: int):
        self.head = Node(l, r)

    def addNode(self, l: int, r: int, v):
        self._addNode(self.head, l, r, v)

    def _addNode(self, root: Node, l, r, v):
        mid = (root.l + root.r) >> 1
        if root.left is None:
            root.left = Node(root.l, mid)
        if root.right is None:
            root.right = Node(mid + 1, root.r)
        if root.l == l and r == root.r:
            root.dirty += v  # point
            root.v += v  # point
            root.sum += v  # point
            return

        self.pushDown(root)
        if r <= mid:
            self._addNode(root.left, l, r, v)
        elif l >= mid + 1:
            self._addNode(root.right, l, r, v)
        else:
            self._addNode(root.left, l, mid, v)
            self._addNode(root.right, mid + 1, r, v)

        root.sum = root.left.sum + root.right.sum

    def query(self, l: int, r: int):
        return self._query(self.head, l, r)

    def _query(self, root: Optional[Node], l: int, r: int):
        if root is None:
            return 0
        if root.l == l and root.r == r:
            return root.sum
        self.pushDown(root)
        mid = (root.l + root.r) >> 1
        if r <= mid:
            return self._query(root.left, l, r)
        if l >= mid + 1:
            return self._query(root.right, l, r)
        # point
        return self._query(root.left, l, mid) + self._query(root.right, mid + 1, r)

    def pushDown(self, root: Node):
        if root.dirty == 0:
            return
        if root.left is not None:
            self._addNode(root.left, root.left.l, root.left.r, root.dirty)
        if root.right is not None:
            self._addNode(root.right, root.right.l, root.right.r, root.dirty)
        root.dirty = 0


class Solution:

    def numberOfPairs1(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [v1 - v2 for v1, v2 in zip(nums1, nums2)]
        segTree = SegTree(-10**9, 10**9)
        ans = 0
        for num in arr:
            v = segTree.query(-10**9, num + diff)
            ans += v
            segTree.addNode(num, num, 1)
        return ans

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [v1 - v2 for v1, v2 in zip(nums1, nums2)]
        s = []
        ans = 0
        for num in arr:
            v = bisect_right(s, num + diff)
            ans += v
            insort(s, num)
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().numberOfPairs([-4, -4, 4, -1, -2, 5], [-2, 2, -1, 4, 4, 3], 1))
    # 3
    print(Solution().numberOfPairs([3, 2, 5], [2, 2, 1], 1))
