"""
 * 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
 * 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
 * 提示：1 <= n <= 10^4
 * 链接：https://leetcode.cn/problems/perfect-squares/
"""
import math


class Solution:

    def numSquares(self, n: int) -> int:
        # 四平方定理 https://baike.baidu.com/item/%E5%9B%9B%E5%B9%B3%E6%96%B9%E5%92%8C%E5%AE%9A%E7%90%86
        # 判断是否为完全平方数
        def isPerfectSquare(x):
            y = int(math.sqrt(x))
            return y * y == x

        # 判断是否能表示为 4^k*(8m+7)
        def checkAnswer4(x):
            while x % 4 == 0:
                x //= 4
            return x % 8 == 7

        if isPerfectSquare(n): return 1
        if checkAnswer4(n): return 4
        i = 1
        while i * i <= n:
            j = n - i * i
            if isPerfectSquare(j): return 2
            i += 1
        return 3


if __name__ == '__main__':
    # 3
    print(Solution().numSquares(12))
    # 2
    print(Solution().numSquares(13))