"""
 * 当 k 个日程安排有一些时间上的交叉时（例如 k 个日程安排都在同一时间内），就会产生 k 次预订。
 * 给你一些日程安排 [start, end) ，请你在每个日程安排添加后，返回一个整数 k ，表示所有先前日程安排会产生的最大 k 次预订。
 * 实现一个 MyCalendarThree 类来存放你的日程安排，你可以一直添加新的日程安排。
 * 1、MyCalendarThree() 初始化对象。
 * 2、int book(int start, int end) 返回一个整数 k ，表示日历中存在的 k 次预订的最大值。
 * 提示：
 * 1、0 <= start < end <= 10^9
 * 2、每个测试用例，调用 book 函数最多不超过 400次
 * 链接：https://leetcode.cn/problems/my-calendar-iii
"""
from typing import Optional


class Node:

    def __init__(self, l: int, r: int, left=None, right=None):
        self.l = l
        self.r = r
        self.dirty = self.max = self.v = 0
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


class SegTree:

    def __init__(self, l: int, r: int):
        self.head = Node(l, r)

    def addNode(self, l: int, r: int, v: int):
        self._addNode(self.head, l, r, v)

    def _addNode(self, root: Optional[Node], l, r, v):
        if root is None: return
        mid = (root.l + root.r) >> 1
        if root.left is None:
            root.left = Node(root.l, mid)
        if root.right is None:
            root.right = Node(mid + 1, root.r)
        if root.l == l and r == root.r:
            root.dirty += v
            root.v += v
            root.max += v
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
        return max(self._query(root.left, l, mid), self._query(root.right, mid + 1, r))

    def pushDown(self, root: Node):
        if root.dirty == 0:
            return
        if root.left is not None:
            self._addNode(root.left, root.left.l, root.left.r, root.dirty)
        if root.right is not None:
            self._addNode(root.right, root.right.l, root.right.r, root.dirty)
        root.dirty = 0


class MyCalendarThree:

    def __init__(self):
        self.segTree = SegTree(0, 10**9)

    def book(self, start: int, end: int) -> int:
        self.segTree.addNode(start, end - 1, 1)
        return self.segTree.head.max


if __name__ == '__main__':
    myCalendarThree = MyCalendarThree()
    print(myCalendarThree.book(10, 20))  #  返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
    print(myCalendarThree.book(50, 60))  #  返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
    print(myCalendarThree.book(10, 40))  #  返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
    print(myCalendarThree.book(5, 15))  #  返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
    print(myCalendarThree.book(5, 10))  #  返回 3
    print(myCalendarThree.book(25, 55))  #  返回 3
