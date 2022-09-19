"""
 * 给你一个下标从 0 开始的二维整数数组 transactions，其中transactions[i] = [cost_i, cashback_i] 。
 * 数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱 money ，为了完成交易 i ，money >= cost_i 这个条件必须为真。
 * 执行交易后，你的钱数 money 变成 money - cost_i + cashback_i 。
 * 请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数 money 是多少。
 * 提示：
 * 1、1 <= transactions.length <= 10^5
 * 2、transactions[i].length == 2
 * 3、0 <= cost_i, cashback_i <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-money-required-before-transactions/
"""

from typing import *


class Solution:

    def minimumMoney(self, transactions: List[List[int]]) -> int:
        n = len(transactions)
        cost_mx = 0
        for transaction in transactions:
            if transaction[1] < transaction[0]:
                cost_mx += transaction[1] - transaction[0]
        ans = 0
        for i, tx in enumerate(transactions):
            if tx[1] > tx[0]:
                ans = max(ans, -(cost_mx - tx[0]))
            else:
                ans = max(ans, -(cost_mx - tx[1]))
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().minimumMoney([[2, 1], [5, 0], [4, 2]]))
    # 3
    print(Solution().minimumMoney([[3, 0], [0, 3]]))
