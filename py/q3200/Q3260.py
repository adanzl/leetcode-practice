"""
 * 给你两个 正整数 n 和 k。
 * 如果整数 x 满足以下全部条件，则该整数是一个 k 回文数：
 * 1、x 是一个 回文数。
 * 2、x 可以被 k 整除。
 * 以字符串形式返回 最大的  n 位 k 回文数。
 * 注意，该整数 不 含前导零。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、1 <= k <= 9
 * 链接：https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/
"""

import sys

sys.setrecursionlimit(5 * 10**5)
INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=3260 lang=python3
# @lcpr version=20001
#
# [3260] 找出最大的 N 位 K 回文数
#


# @lc code=start
class Solution:

    def largestPalindrome(self, n: int, k: int) -> str:
        # 最小的 n // 2 位数 0...0k
        pow10 = [1]
        m = (n + 1) // 2
        for _ in range(n + 1):
            pow10.append(pow10[-1] * 10 % k)
        ans = [''] * n
        vis = [[False] * k for _ in range(m + 1)]

        def dfs(i, j):
            # 填第i位，MOD k为j
            if i == m: return j == 0
            vis[i][j] = True
            for d in range(9, -1, -1):
                if n % 2 and i == m - 1:  # 中间
                    j2 = (j + d * pow10[i]) % k
                else:
                    j2 = (j + d * (pow10[i] + pow10[n - 1 - i])) % k
                if not vis[i + 1][j2] and dfs(i + 1, j2):
                    ans[i] = ans[n - 1 - i] = str(d)
                    return True
            return False

        dfs(0, 0)
        return ''.join(ans)


# @lc code=end

if __name__ == '__main__':
    # ''
    print(Solution().largestPalindrome(10**5, 6))
    # '595'
    print(Solution().largestPalindrome(3, 5))
    # '8'
    print(Solution().largestPalindrome(1, 4))
    # '89898'
    print(Solution().largestPalindrome(5, 6))
