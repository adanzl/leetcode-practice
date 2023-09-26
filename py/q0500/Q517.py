"""
 * 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
 * 在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
 * 给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。
 * 如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。
 * 提示：
 * 1、n == machines.length
 * 2、1 <= n <= 10^4
 * 3、0 <= machines[i] <= 10^5
 * 链接：https://leetcode.cn/problems/super-washing-machines/
"""

from typing import List

#
# @lc app=leetcode.cn id=517 lang=python3
#
# [517] 超级洗衣机
#


# @lc code=start
class Solution:

    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        sm = sum(machines)
        a, r = divmod(sm, n)
        if r: return -1
        ans, s = 0, 0
        for num in machines:
            num -= a
            s += num  # 前 i 项和 减去 a*i
            ans = max(ans, abs(s), num)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 0
    print(Solution().findMinMoves([0, 0]))
    # 2
    print(Solution().findMinMoves([0, 3, 0]))
    # 8
    print(Solution().findMinMoves([0, 0, 11, 5]))
    # 3
    print(Solution().findMinMoves([1, 0, 5]))
    # -1
    print(Solution().findMinMoves([0, 2, 0]))
