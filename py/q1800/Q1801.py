"""
 * 给你一个二维整数数组 orders ，其中每个 orders[i] = [price_i, amount_i, orderType_i] 表示有 amount_i 笔类型为 orderType_i 、价格为 price_i 的订单。
 * 订单类型 orderType_i 可以分为两种：
 * 1、0 表示这是一批采购订单 buy
 * 2、1 表示这是一批销售订单 sell
 * 注意，orders[i] 表示一批共计 amount_i 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 i ，由 orders[i] 表示的所有订单提交时间均早于 orders[i+1] 表示的所有订单。
 * 存在由未执行订单组成的 积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：
 * 1、如果该订单是一笔采购订单 buy ，则可以查看积压订单中价格 最低 的销售订单 sell 。
 *    如果该销售订单 sell 的价格 低于或等于 当前采购订单 buy 的价格，则匹配并执行这两笔订单，并将销售订单 sell 从积压订单中删除。
 *    否则，采购订单 buy 将会添加到积压订单中。
 * 2、反之亦然，如果该订单是一笔销售订单 sell ，则可以查看积压订单中价格 最高 的采购订单 buy 。
 *    如果该采购订单 buy 的价格 高于或等于 当前销售订单 sell 的价格，则匹配并执行这两笔订单，并将采购订单 buy 从积压订单中删除。
 *    否则，销售订单 sell 将会添加到积压订单中。
 * 输入所有订单后，返回积压订单中的 订单总数 。由于数字可能很大，所以需要返回对 10^9 + 7 取余的结果。
 * 提示：
 * 1、1 <= orders.length <= 10^5
 * 2、orders[i].length == 3
 * 3、1 <= price_i, amount_i <= 10^9
 * 4、orderType_i 为 0 或 1
 * 链接：https://leetcode.cn/problems/number-of-orders-in-the-backlog/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        h_buy, h_sell = [], []  # price, amount
        for price, amount, order_type in orders:
            if order_type == 0:  # buy
                while h_sell and h_sell[0][0] <= price and amount > 0:
                    if h_sell[0][1] <= amount:
                        amount -= h_sell[0][1]
                        heappop(h_sell)
                    else:
                        h_sell[0][1] -= amount
                        amount = 0
                if amount > 0:
                    heappush(h_buy, [-price, amount])
            else:  # sell
                while h_buy and -h_buy[0][0] >= price and amount > 0:
                    if h_buy[0][1] <= amount:
                        amount -= h_buy[0][1]
                        heappop(h_buy)
                    else:
                        h_buy[0][1] -= amount
                        amount = 0
                if amount > 0:
                    heappush(h_sell, [price, amount])
        return (sum([amount for _, amount in h_buy]) + sum([amount for _, amount in h_sell])) % MOD


if __name__ == '__main__':
    # 39
    print(Solution().getNumberOfBacklogOrders([[19,28,0],[9,4,1],[25,15,1]]))
    # 6
    print(Solution().getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]))
    # 999999984
    print(Solution().getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]))