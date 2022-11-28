"""
 * 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：
 * 1、如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
 * 2、如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
 * 如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：
 * 1、在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
 * 2、在关门期间，如果某一个小时有顾客到达，代价增加 1 。
 * 请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
 * 注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。
 * 提示：
 * 1、1 <= customers.length <= 10^5
 * 2、customers 只包含字符 'Y' 和 'N' 。
 * 链接：https://leetcode.cn/problems/minimum-penalty-for-a-shop/
"""
from itertools import accumulate


class Solution:

    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        arr1 = [0 if c == 'Y' else 1 for c in customers]
        arr2 = [1 if c == 'Y' else 0 for c in customers]
        p_s1 = [0] + list(accumulate(arr1))
        p_s2 = [0] + list(accumulate(arr2))
        ans = -1
        cost = 0x3c3c3c3c
        for i in range(n + 1):
            c = p_s2[n] - p_s2[i] + p_s1[i]
            if c < cost:
                cost = c
                ans = i
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().bestClosingTime("YYNY"))
    # 0
    print(Solution().bestClosingTime("NNNNN"))
    # 4
    print(Solution().bestClosingTime("YYYY"))