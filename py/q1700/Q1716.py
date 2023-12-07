"""
 * Herby 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。
 * 最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。
 * 在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。
 * 给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。
 * 提示：1 <= n <= 1000
 * 链接：https://leetcode.cn/problems/calculate-money-in-leetcode-bank
"""

#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#


# @lc code=start
class Solution:

    def totalMoney(self, n: int) -> int:
        a, r = divmod(n, 7)
        return a * 28 + (a - 1) * a // 2 * 7 + a * r + (1 + r) * r // 2


# @lc code=end

if __name__ == '__main__':
    # 10
    print(Solution().totalMoney(4))
    # 37
    print(Solution().totalMoney(10))
    # 96
    print(Solution().totalMoney(20))
