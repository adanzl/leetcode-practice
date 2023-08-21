"""
 * 一开始，你的银行账户里有 100 块钱。
 * 给你一个整数purchaseAmount ，它表示你在一次购买中愿意支出的金额。
 * 在一个商店里，你进行一次购买，实际支出的金额会向 最近 的 10 的 倍数 取整。
 * 换句话说，你实际会支付一个 非负 金额 roundedAmount ，满足 roundedAmount 是 10 的倍数且 abs(roundedAmount - purchaseAmount) 的值 最小 。
 * 如果存在多于一个最接近的 10 的倍数，较大的倍数 是你的实际支出金额。
 * 请你返回一个整数，表示你在愿意支出金额为 purchaseAmount 块钱的前提下，购买之后剩下的余额。
 * 注意：0 也是 10 的倍数。
 * 提示：0 <= purchaseAmount <= 100
 * 链接：https://leetcode.cn/problems/account-balance-after-rounded-purchase/
"""


class Solution:

    def accountBalanceAfterPurchase(self, pa: int) -> int:
        return 100 - (pa + 5) // 10 * 10  # 个位数 四舍五入 公式


if __name__ == '__main__':
    # 90
    print(Solution().accountBalanceAfterPurchase(9))
    # 90
    print(Solution().accountBalanceAfterPurchase(10))
    # 80
    print(Solution().accountBalanceAfterPurchase(15))