"""
 * Alice 把 n 个气球排列在一根绳子上。给你一个下标从 0 开始的字符串 colors ，其中 colors[i] 是第 i 个气球的颜色。
 * Alice 想要把绳子装扮成 彩色 ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 彩色 。
 * 给你一个下标从 0 开始的整数数组 neededTime ，其中 neededTime[i] 是 Bob 从绳子上移除第 i 个气球需要的时间（以秒为单位）。
 * 返回 Bob 使绳子变成 彩色 需要的 最少时间 。     
 * 提示：
 * 1、n == colors.length == neededTime.length
 * 2、1 <= n <= 10^5
 * 3、1 <= neededTime[i] <= 10^4
 * 4、colors 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/minimum-time-to-make-rope-colorful/
"""
from typing import *


class Solution:

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        cost = 0
        for i in range(len(colors)):
            ans += neededTime[i]
            if colors[i - 1] != colors[i]:
                ans -= cost
                cost = 0
            cost = max(cost, neededTime[i])
        ans -= cost
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minCost("abaac", [1, 2, 3, 4, 5]))
    # 0
    print(Solution().minCost("abc", [1, 2, 3]))
    # 2
    print(Solution().minCost("aabaa", [1, 2, 3, 4, 1]))
    # 26
    print(Solution().minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
