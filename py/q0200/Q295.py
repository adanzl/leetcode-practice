"""
 * 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
 * 例如，
 * [2,3,4] 的中位数是 3
 * [2,3] 的中位数是 (2 + 3) / 2 = 2.5
 * 设计一个支持以下两种操作的数据结构：
 * 1、void addNum(int num) - 从数据流中添加一个整数到数据结构中。
 * 2、double findMedian() - 返回目前所有元素的中位数。
 * 进阶:
 * 1、如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 2、如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 链接：https://leetcode.cn/problems/find-median-from-data-stream/
"""
from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.ql = []  # 大顶堆 len(self.ql) >= len(self.qr)
        self.qr = []  # 小顶堆

    def addNum(self, num: int) -> None:
        # 小则放左边，否则右边
        if not self.ql or -self.ql[0] >= num:
            heappush(self.ql, -num)
        else:
            heappush(self.qr, num)
        while len(self.ql) < len(self.qr):
            heappush(self.ql, -heappop(self.qr))
        while len(self.ql) - len(self.qr) > 1:
            heappush(self.qr, -heappop(self.ql))

    def findMedian(self) -> float:
        return -self.ql[0] if len(self.ql) > len(self.qr) else (-self.ql[0] + self.qr[0]) / 2
