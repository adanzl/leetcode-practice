"""
 * 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
 * 实现 SummaryRanges 类：
 * 1、SummaryRanges() 使用一个空数据流初始化对象。
 * 2、void addNum(int val) 向数据流中加入整数 val 。
 * 3、int[][] getIntervals() 以不相交区间 [start_i, end_i] 的列表形式返回对数据流中整数的总结。
 * 提示：
 * 1、0 <= val <= 10^4
 * 2、最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
 * 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
 * 链接：https://leetcode.cn/problems/data-stream-as-disjoint-intervals/
"""
from typing import List
from sortedcontainers import SortedDict


class SummaryRanges:

    def __init__(self):
        self.nums = SortedDict()

    def addNum(self, value: int) -> None:
        i_lk = self.nums.bisect(value) - 1
        i_rk = self.nums.bisect(value)
        lk = self.nums.keys()[i_lk] if 0 <= i_lk < len(self.nums) else None
        rk = self.nums.keys()[i_rk] if 0 <= i_rk < len(self.nums) else None
        l = r = value
        if lk is not None and self.nums[lk] >= value:
            return
        if lk is not None and self.nums[lk] == value - 1:
            self.nums[lk] = value
            l = lk
        if rk == value + 1:
            self.nums[l] = self.nums[rk]
            del self.nums[rk]
            return
        self.nums[l] = r

    def getIntervals(self) -> List[List[int]]:
        return [[k, v] for k, v in self.nums.items()]  # type: ignore


if __name__ == '__main__':
    obj = SummaryRanges()
    obj.addNum(1)  # arr = [1]
    print(obj.getIntervals())  # 返回 [[1, 1]]
    obj.addNum(3)  # arr = [1, 3]
    print(obj.getIntervals())  # 返回 [[1, 1], [3, 3]]
    obj.addNum(7)  # arr = [1, 3, 7]
    print(obj.getIntervals())  # 返回 [[1, 1], [3, 3], [7, 7]]
    obj.addNum(2)  # arr = [1, 2, 3, 7]
    print(obj.getIntervals())  # 返回 [[1, 3], [7, 7]]
    obj.addNum(6)  # arr = [1, 2, 3, 6, 7]
    print(obj.getIntervals())  # 返回 [[1, 3], [6, 7]]
    obj.addNum(8)
    print(obj.getIntervals())
    obj.addNum(4)
    print(obj.getIntervals())
    obj.addNum(5)
    print(obj.getIntervals())
    obj.addNum(8)
    print(obj.getIntervals())
    obj.addNum(8)
    print(obj.getIntervals())
    obj.addNum(8)
    print(obj.getIntervals())
