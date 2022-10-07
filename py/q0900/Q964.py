"""
 * 给定一个正整数 x，我们将会写出一个形如 x (op1) x (op2) x (op3) x ... 的表达式，其中每个运算符 op1，op2，… 可以是加、减、乘、除（+，-，*，或是 /）之一。
 * 例如，对于 x = 3，我们可以写出表达式 3 * 3 / 3 + 3 - 3，该式的值为 3 。
 * 在写这样的表达式时，我们需要遵守下面的惯例：
 * 1、除运算符（/）返回有理数。
 * 2、任何地方都没有括号。
 * 3、我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。
 * 4、不允许使用一元否定运算符（-）。例如，“x - x” 是一个有效的表达式，因为它只使用减法，但是 “-x + x” 不是，因为它使用了否定运算符。 
 * 我们希望编写一个能使表达式等于给定的目标值 target 且运算符最少的表达式。返回所用运算符的最少数量。
 * 提示：
 * 1、2 <= x <= 100
 * 2、1 <= target <= 2 * 10^8
 * 链接：https://leetcode.cn/problems/least-operators-to-express-number/
"""
from functools import cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        @cache
        def dfs(t):
            if x == t: return 1
            if x > t:
                return min(t * 2, (x - t) * 2 + 1)
            n = 1
            num = x
            while num < t:
                num *= x
                n += 1
            if num == t: return n
            if num - t >= t:  # 如果反向距离大于目标距离，就只处理正向距离
                return n - 1 + dfs(t - num // x)
            return min(n - 1 + dfs(t - num // x), n + dfs(num - t))

        return dfs(target) - 1


if __name__ == '__main__':
    # 13
    print(Solution().leastOpsExpressTarget(14, 5040))
    # 3
    print(Solution().leastOpsExpressTarget(3, 5))
    # 5
    print(Solution().leastOpsExpressTarget(3, 19))
    # 8
    print(Solution().leastOpsExpressTarget(5, 501))
    # 3
    print(Solution().leastOpsExpressTarget(100, 100000000))