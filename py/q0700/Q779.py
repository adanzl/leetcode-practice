"""
 * 我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
 * 例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
 * 给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）
 * 提示:
 * 1、1 <= n <= 30
 * 2、1 <= k <= 2^n - 1
 * 链接：https://leetcode.cn/problems/k-th-symbol-in-grammar/
"""
from typing import List


class Solution:

    def kthGrammar(self, n: int, k: int) -> int:

        def f(idx):
            if idx == 0: return 0
            if idx & 1 == 0:  # even
                return 0 if f(idx // 2) == 0 else 1
            else:  # odd
                return 1 if f((idx - 1) // 2) == 0 else 0

        return f(k - 1)


if __name__ == '__main__':
    # 0
    print(Solution().kthGrammar(30, 434991989))
    # 0
    print(Solution().kthGrammar(1, 1))
    # 0
    print(Solution().kthGrammar(2, 1))
    # 1
    print(Solution().kthGrammar(2, 2))
