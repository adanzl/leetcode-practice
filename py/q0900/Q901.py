"""
 * 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
 * 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
 * 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。
 * 提示：
 * 1、调用 StockSpanner.next(int price) 时，将有 1 <= price <= 10^5。
 * 2、每个测试用例最多可以调用  10000 次 StockSpanner.next。
 * 3、在所有测试用例中，最多调用 150000 次 StockSpanner.next。
 * 4、此问题的总时间限制减少了 50%。
 * 链接：https://leetcode.cn/problems/online-stock-span/
"""
from typing import Deque


class StockSpanner:

    def __init__(self):
        self.s = Deque()

    def next(self, price: int) -> int:
        cnt = 1
        while self.s and self.s[-1][0] <= price:
            cnt += self.s.pop()[1]
        self.s.append([price, cnt])
        return cnt


if __name__ == '__main__':
    s = StockSpanner()
    print(s.next(100))  # 1
    print(s.next(80))  # 1
    print(s.next(60))  # 1
    print(s.next(70))  # 2
    print(s.next(60))  # 1
    print(s.next(75))  # 4
    print(s.next(85))  # 6
