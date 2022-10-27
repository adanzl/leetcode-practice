"""
 * 给你 n 笔订单，每笔订单都需要快递服务。
 * 请你统计所有有效的 收件/配送 序列的数目，确保第 i 个物品的配送服务 delivery(i) 总是在其收件服务 pickup(i) 之后。
 * 由于答案可能很大，请返回答案对 10^9 + 7 取余的结果。
 * 提示：1 <= n <= 500
 * 链接：https://leetcode.cn/problems/count-all-valid-pickup-and-delivery-options/
"""


class Solution:

    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        for i in range(1, n):  # 2*i-1 pos
            ans *= (i + 1) * (2 * i + 1)
            ans %= MOD
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().countOrders(1))
    # 6
    print(Solution().countOrders(2))
    # 90
    print(Solution().countOrders(3))
    #
    print(Solution().countOrders(500))
