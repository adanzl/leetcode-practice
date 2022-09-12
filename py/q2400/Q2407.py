from typing import *
'''
给你一个整数数组 nums 和一个整数 k 。
找到 nums 中满足以下要求的最长子序列：
1、子序列 严格递增
2、子序列中相邻元素的差值 不超过 k 。
请你返回满足上述要求的 最长子序列 的长度。
子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
提示：
1、1 <= nums.length <= 10^5
2、1 <= nums[i], k <= 10^5
链接：https://leetcode.cn/problems/longest-increasing-subsequence-ii
'''


class Node:

    def __init__(self, l: int, r: int):
        self. l = l
        self. r = r
        self.dirty = self.max = self.v = 0
        self.left = None
        self.right = None


class SegTree:
    # 动态开点线段树模板，取最大值
    def __init__(self, l: int, r: int):
        self.head = Node(l, r)

    def addNode(self, l: int, r: int, v):
        self._addNode(self.head, l, r, v)

    def _addNode(self, root: Node,  l,  r,  v):
        mid = (root.l + root.r) >> 1
        if root.left is None:
            root.left = Node(root.l, mid)
        if root.right is None:
            root.right = Node(mid + 1, root.r)
        if root.l == l and r == root.r:
            root.dirty = 1
            root.v = v
            root.max = v
            return

        self.pushDown(root)
        if r <= mid:
            self._addNode(root.left, l, r, v)
        elif l >= mid + 1:
            self._addNode(root.right, l, r, v)
        else:
            self._addNode(root.left, l, mid, v)
            self._addNode(root.right, mid + 1, r, v)

        root.max = max(root.left.max, root.right.max)

    def query(self, l: int, r: int):
        return self._query(self.head, l, r)

    def _query(self,  root: Node,  l: int,  r: int):
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
        return max(self._query(root.left, l, mid), self._query(root.right, mid + 1, r))

    def pushDown(self, root: Node):
        if root.dirty == 0:
            return
        self._addNode(root.left, root.left.l, root.left.r, root.left.v)
        self._addNode(root.right, root.right.l, root.right.r, root.right.v)
        root.dirty = 0


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        segTree = SegTree(0, 200_001)
        for num in nums:
            mx = segTree.query(num - k, num - 1)
            segTree.addNode(num, num, mx + 1)
        return segTree.head.max


if __name__ == '__main__':
    # 5
    print(Solution().lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3))
    # 4
    print(Solution().lengthOfLIS([7, 4, 5, 1, 8, 12, 4, 7], 5))
    # 1
    print(Solution().lengthOfLIS([1, 5], 1))
