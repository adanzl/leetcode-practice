"""
 * 给你一个正整数 n ，开始时，它放在桌面上。在 10^9 天内，每天都要执行下述步骤：
 * 1、对于出现在桌面上的每个数字 x ，找出符合 1 <= i <= n 且满足 x % i == 1 的所有数字 i 。
 * 2、然后，将这些数字放在桌面上。
 * 返回在 10^9 天之后，出现在桌面上的 不同 整数的数目。
 * 注意：
 * 1、一旦数字放在桌面上，则会一直保留直到结束。
 * 2、% 表示取余运算。例如，14 % 3 等于 2 。
 * 提示：1 <= n <= 100
 * 链接：https://leetcode.cn/problems/count-distinct-numbers-on-board
"""

#
# @lc app=leetcode.cn id=2549 lang=python3
#
# [2549] 统计桌面上的不同数字
#


# @lc code=start
from typing import Deque


class Solution:

    def distinctIntegers(self, n: int) -> int:
        ans = set([n])
        q = Deque([n])
        while q:
            x  = q.popleft()
            for i in range(1, n + 1):
                if x % i == 1 and i not in ans:
                    ans.add(i)
                    q.append(i)
        return len(ans)


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().distinctIntegers(5))
    # 2
    print(Solution().distinctIntegers(3))
    #
    # print(Solution().distinctIntegers())
